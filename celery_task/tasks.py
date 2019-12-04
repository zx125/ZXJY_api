from .celery import app

from home.models import Banner
from django.conf import settings
from django.core.cache import cache
from home.serializers import BannerModelSerializer
@app.task
def update_banner_cache():
    banner_query = Banner.objects.filter(is_delete=False, is_show=True).order_by('-order')[:settings.BANNER_COUNT]
    #序列化
    banner_list = BannerModelSerializer(banner_query, many=True).data
    #给图片拼接正确的请求路径
    for banner_dic in banner_list:
        banner_dic['image'] = settings.BASE_URL + banner_dic['image']
    print(cache.get('banner_list'))
    cache.set('banner_list', banner_list)
