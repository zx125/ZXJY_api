from django.db import models

# Create your models here.
from utils.model import BaseModel
class Banner(BaseModel):
    title = models.CharField(max_length=16, verbose_name='标题')
    link = models.CharField(max_length=64, verbose_name='链接')
    image = models.ImageField(upload_to='banner', verbose_name='图片链接')
    info = models.TextField(verbose_name='轮播图简介')
    order = models.IntegerField(verbose_name='显示顺序')

    class Meta:
        db_table = 'lufei_banner'
        verbose_name_plural = '轮播图表'

    def __str__(self):
        return self.title
