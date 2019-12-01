from django.urls import path, re_path
from . import views
urlpatterns = [
    # 多方式登录
    path('login', views.LoginAPIView.as_view()),
    # 手机验证码登录
    path('login/mobile', views.LoginMobileAPIView.as_view()),
    # 手机验证码注册
    path('register', views.RegisterAPIView.as_view()),
    # 发送短信
    path('sms', views.SMSAPIView.as_view()),
    # 手机注册验证
    path('mobile', views.MobileAPIView.as_view()),
]
