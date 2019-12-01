from django.shortcuts import render

# Create your views here.
from . import models,serializers
from rest_framework.generics import ListAPIView
class BannerListAPIView(ListAPIView):
    queryset = models.Banner.objects.filter(is_delete=False,is_show=True).order_by('-order').all()
    serializer_class = serializers.BannerModelSerializer