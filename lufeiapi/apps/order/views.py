from rest_framework.response import Response

# Create your views here.
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . import serializers
from rest_framework.views import APIView
class PayAPIView(APIView):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_class = [IsAuthenticated]
    def post(self,request,*args,**kwargs):
        serializer = serializers.OrderModelSerializer(data=request.data,context={'request':request})
        # 信息校验
        serializer.is_valid(raise_exception=True)
        # 订单入库
        serializer.save()
        # 返回一个支付链接
        return Response(serializer.pay_url)


from libs.iPay import alipay
from .models import *
from utils.logging import logger

class SuccessAPIView(APIView):
    # 重点：要不要做登录认证，不需要：订单号可以获取你所需要的所有信息、回调参数有自己的安全校验、支付宝永远不可能通过token
    def patch(self, request, *args, **kwargs):

        #获取上传的信息
        data = request.query_params.dict()

        #sign签名必须被取出
        sign = data.pop('sign')
        #拿签名做数据校验
        result = alipay.verify(data, sign)
        if result:
            # 一般不在同步回调直接操作订单状态
            pass
            # models.Order.objects.filter(out_trade_no=data.get('out_trade_no')).update(order_status=1)
        return Response('同步回调完成')

    # 异步支付宝回调接口：公网下才能验证
    def post(self, request, *args, **kwargs):
        data = request.data.dict()  # 回调参数，是QueryDict类型，不能直接调用pop方法
        sign = data.pop('sign')  # 签名
        out_trade_no = data.get('out_trade_no')  # 订单号
        result = alipay.verify(data, sign)
        if result and data["trade_status"] in ("TRADE_SUCCESS", "TRADE_FINISHED" ):
            try:
                order = models.Order.objects.get(out_trade_no=out_trade_no)
                if order.order_status != 1:
                    order.order_status = 1
                    order.save()
                    logger.warning('%s订单完成支付' % out_trade_no)
                return Response('success')
            except:
                pass
        return Response('failed')