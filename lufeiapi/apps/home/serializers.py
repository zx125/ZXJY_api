from rest_framework.serializers import ModelSerializer

from . import models

class BannerModelSerializer(ModelSerializer):
    class Meta:
        model = models.Banner
        fields = ('title','link','image')