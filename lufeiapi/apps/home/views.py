from django.shortcuts import render

from rest_framework.response import Response
# Create your views here.
from . import models,serializers
from django.core.cache import cache
from django.conf import settings
from rest_framework.generics import ListAPIView
# 访问量大且数据一段时间内较为固定的接口，可以左接口缓存
# 1）从缓存中拿，有直接返回，没有查询数据库
# 2）查询数据库的数据返回给前台，同时将数据建立缓存
class BannerListAPIView(ListAPIView):
    queryset = models.Banner.objects.filter(is_delete=False, is_show=True).order_by('-order')[:settings.BANNER_COUNT]
    serializer_class = serializers.BannerModelSerializer

    def get(self, request, *args, **kwargs):
        banner_list = cache.get('banner_list')
        print(banner_list)
        if not banner_list:
            print('走数据库了')
            response = self.list(request, *args, **kwargs)
            # response.data不是json数据，是drf中的自定义ReturnList类
            cache.set('banner_list', response.data)  # 缓存不设过期时间，更新任务交给celery异步任务框架
            return response
        print('缓存了')
        return Response(banner_list)