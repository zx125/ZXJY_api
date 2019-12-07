from django.urls import path, re_path

from . import views
urlpatterns = [
    #支付接口
    path('pay', views.PayAPIView.as_view()),
    #支付前端回调接口
    path('success', views.SuccessAPIView.as_view()),
]