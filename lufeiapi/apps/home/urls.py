from django.urls import path, re_path

from . import views
urlpatterns = [
    path('banners', views.BannerListAPIView.as_view()),
]