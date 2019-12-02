import re

from rest_framework import serializers
from django.core.cache import cache
from django.conf import settings
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from . import models
#多方式登录
class LoginModelSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = models.User
        fields = ('username','password')

    # 校验user，签发token，保存到serializer
    # 那种drf-jwt
    def validate(self, attrs):
        # user = authenticate(**attrs)
        # 账号密码登录 => 多方式登录
        user = self._many_method_login(**attrs)

        # 签发token，并将user和token存放到序列化对象中
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        self.user = user
        self.token = token

        return attrs

    def _many_method_login(self,**attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if re.match(r'.*@.*', username):
            user = models.User.objects.filter(email=username).first()  # type: models.User

        elif re.match(r'^1[3-9][0-9]{9}$', username):
            user = models.User.objects.filter(mobile=username).first()
        else:
            user = models.User.objects.filter(username=username).first()

        if not user:
            raise serializers.ValidationError({'username': '账号有误'})

        if not user.check_password(password):
            raise serializers.ValidationError({'password': '密码有误'})

        return user


class LoginMobileSerializer(serializers.ModelSerializer):
    mobile = serializers.CharField(write_only=True,min_length=11,max_length=11)
    code = serializers.CharField(write_only=True,min_length=4,max_length=4)

    class Meta:
        model = models.User
        fields = ('mobile','code')

    def validate_mobile(self,value):
        if re.match(r'^1[3-9][0-9]{9}$',value):
            return value
        raise serializers.ValidationError('手机号码格式有误')

    def validate_code(self,value):
        #验证码全是数字
        try:
            int(value)
            return value
        except:
            raise serializers.ValidationError('验证码格式有误')

    def validate(self, attrs):
        user = self._get_user(**attrs)

        #签发token
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        self.user = user
        self.token = token

        return attrs

    def _get_user(self,**attrs):
        mobile = attrs.get('mobile')
        code = attrs.get('code')
        user = models.User.objects.filter(mobile=mobile).first()
        if not user:
            raise serializers.ValidationError({'mobile':'该手机未注册'})

        old_code = cache.get(settings.SMS_CACHE_KEY %mobile)
        print(old_code)
        if code != old_code:
            raise serializers.ValidationError({'code':'验证码错误'})
        return user

class RegisterMobileSerializer(serializers.ModelSerializer):
    code = serializers.CharField(write_only=True,min_length=4,max_length=4)
    class Meta:
        model = models.User
        fields = ('mobile','code','password')
        extra_kwargs = {
            'mobile':{
                'min_length':11,
                'max_length':11
            },
            'password':{
                'min_length':6,
                'max_length':18
            }
        }

    def validate_mobile(self,value):
        if re.match(r'^1[3-9][0-9]{9}$',value):
            return value
        raise serializers.ValidationError('手机号码有误')

    def validate_code(self, value):
        try:
            int(value)
            return value
        except:
            raise serializers.ValidationError('验证码格式有误')

    def validate_password(self, value):
        # 密码不能包含或必须包含哪些字符
        return value

    # 拿出不入库的数据，塞入额外要入库的数据
    def validate(self, attrs):
        mobile = attrs.get('mobile')
        code = attrs.pop('code')
        old_code = cache.get(settings.SMS_CACHE_KEY % mobile)
        if code != old_code:
            raise serializers.ValidationError({'code': '验证码有误'})
        # cache.set(settings.SMS_CACHE_KEY % mobile, '0000', 0)  # 清除一次性验证码

        attrs['username'] = mobile
        attrs['email'] = '%s@oldboy.com' % mobile

        return attrs

    def create(self, validated_data):
        return models.User.objects.create_user(**validated_data)
