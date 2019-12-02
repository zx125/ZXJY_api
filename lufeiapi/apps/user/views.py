
import re
from rest_framework.views import APIView
from utils.response import APIResponse
from django.conf import settings
from . import models,serializers,throttles
from django.core.cache import cache
from libs import tx_sms
from django.conf import settings

# 多方式登录
class LoginAPIView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = serializers.LoginModelSerializer(data=request.data)
        if serializer.is_valid():
            return APIResponse(data={
                'username':serializer.user.username,
                'token':serializer.token
            })
        return APIResponse(1,'failed',data=serializer.errors,http_status=400)


# 发送短信
class SMSAPIView(APIView):
    throttle_classes = [throttles.SMSRateThrottle]

    def post(self, request, *args, **kwargs):
        # 拿到前台手机
        mobile = request.data.get('mobile')
        if not (mobile and re.match(r'^1[3-9][0-9]{9}$', mobile)):
            return APIResponse(2, '手机号格式有误')
        # 获取验证码
        code = tx_sms.get_code()
        # 发送短信
        result = tx_sms.send_sms(mobile, code, settings.SMS_EXP // 60)
        # 服务器缓存验证码
        if not result:
            return APIResponse(1, '发送验证码失败')
        cache.set(settings.SMS_CACHE_KEY % mobile, code, settings.SMS_EXP)
        # 校验发送的验证码与缓存的验证码是否一致
        # print('>>>> %s - %s <<<<' % (code, cache.get('sms_%s' % mobile)))
        return APIResponse(0, '发送验证码成功')


# 手机验证码登录
class LoginMobileAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self,request,*args,**kwargs):
        serializer = serializers.LoginMobileSerializer(data=request.data)
        if serializer.is_valid():
            return APIResponse(
                data = {
                    'username':serializer.user.username,
                    'token':serializer.token
                }
            )
        return APIResponse(1,'failed',data = serializer.errors,http_status=400)


# 手机验证码注册
class RegisterAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self,request,*args,**kwargs):
        serializer = serializers.RegisterMobileSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return APIResponse(0,'注册成功',data={
                'username':obj.username,
                'mobile':obj.mobile,
                'email':obj.email,
            })
        return APIResponse(1,'注册失败',data=serializer.errors,http_status=400)


# 手机号码验证
class MobileAPIView(APIView):
    def post(self,request,*args,**kwargs):
        mobile = request.data.get('mobile')

        if not (mobile and re.match(r'^1[3-9][0-9]{9}$',mobile)):
            return APIResponse(2,"手机号格式有误")

        try:
            models.User.objects.get(mobile=mobile)
            return APIResponse(1,'手机号已注册')
        except:
            return APIResponse(0,'手机未注册')