import time
from rest_framework import serializers

from . import models
from course.models import Course

from libs.iPay import alipay, alipay_gateway
from django.conf import settings

class OrderModelSerializer(serializers.ModelSerializer):
    # 商品的主键们：暂定 '1,2,3' 方式传多个主键
    goods_pks = serializers.CharField(max_length=64)

    class Meta:
        model = models.Order
        fields = (
            'subject',
            'total_amount',
            'pay_type',
            'goods_pks',
        )
        extra_kwargs = {
            'total_amount': {
                'required': True
            }
        }

    # 后台要根据所有的主键和总价，校验价格（防止传输中被修改）
    def validate(self, attrs):
        goods_pks = attrs.pop('goods_pks')
        goods_pks = [pk for pk in goods_pks.split(',')]
        goods_objs = []
        for pk in goods_pks:
            try:
                obj = Course.objects.get(pk=pk)
                goods_objs.append(obj)
            except:
                raise serializers.ValidationError({'pk': '课程主键有误'})

        total_price = 0
        for good in goods_objs:
            total_price += good.price

        # 商品总价
        total_amount = attrs.get('total_amount')
        if total_price != total_amount:
            raise serializers.ValidationError({'total_amount': '价格被恶意篡改'})

        # 生成订单号
        order_on = self._get_order_no()
        # 订单名
        subject = attrs.get('subject')

        # 生成订单链接
        order_params = alipay.api_alipay_trade_page_pay(out_trade_no=order_on,
                                                        total_amount=float(total_amount),
                                                        subject=subject,
                                                        return_url=settings.RETURN_URL,  # 同步回调的前台接口
                                                        notify_url=settings.NOTIFY_URL  # 异步回调的后台接口
                                                        )
        pay_url = alipay_gateway + order_params

        # 将支付链接保存在serializer对象中
        self.pay_url = pay_url

        # 添加额外的入口字段
        attrs['out_trade_no'] = order_on
        # 视图类给序列化类传参
        attrs['user'] = self.context.get('request').user

        # 将所有的商品对象存放在校验数据中，辅助订单详情表商品信息的入库
        attrs['courses'] = goods_objs

        # 代表校验通过
        return attrs


    # 重写create方法，完成订单表和订单详情表入库操作
    def create(self, validated_data):
        courses = validated_data.pop('courses')

        #调用父类create方法完成订单表入库
        order = super().create(validated_data)

        # 关系表操作
        order_detail_list = []
        for course in courses:
            order_detail_list.append(models.OrderDetail(order=order, course=course, price=course.price, real_price=course.price))

        # 将多个订单详情对象，批量入库
        models.OrderDetail.objects.bulk_create(order_detail_list)

        return order

    def _get_order_no(self):
        no = '%s' % time.time()
        return no.replace('.', '', 1)
