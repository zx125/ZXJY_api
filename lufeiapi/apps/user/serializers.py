import re

from rest_framework import serializers
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from . import models
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
