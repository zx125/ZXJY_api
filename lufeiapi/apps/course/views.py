from rest_framework.generics import ListAPIView

from . import models, serializers

# OrderingFilter排序、SearchFilter搜索
from rest_framework.filters import OrderingFilter, SearchFilter
# 自定义
from .filters import LimitFilter
# 分页
from .paginations import CoursePageNumberPagination, CourseLimitOffsetPagination, CourseCursorPagination

# 分类筛选：django-filter：filter_backends配置DjangoFilterBackend，再在filter_fields中配置分组筛选的字段
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CourseFilterSet

class FreeCourseListAPIView(ListAPIView):
    queryset = models.Course.objects.filter(is_delete=False, is_show=True).order_by('-orders').all()
    serializer_class = serializers.FreeCourseModelSerializer

    # 配置过滤器类
    # filter_backends = [OrderingFilter, LimitFilter]  # LimitFilter自定义过滤器
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    # 参与排序的字段: ordering=-price,id
    ordering_fields = ['price', 'id', 'students']
    # 参与搜索的字段: search=python  (name字段中带python就ok)
    search_fields = ['name', 'brief']
    # 参与分类筛选的字段：所有字段都可以，但是用于分组的字段更有意义
    # filter_fields = ['course_category']
    filter_class = CourseFilterSet

    # 分页器
    pagination_class = CoursePageNumberPagination
    # pagination_class = CourseLimitOffsetPagination
    # pagination_class = CourseCursorPagination


class CategoryListAPIView(ListAPIView):
    queryset = models.CourseCategory.objects.filter(is_delete=False, is_show=True).order_by('orders').all()
    serializer_class = serializers.CategoryModelSerializer


from rest_framework.generics import RetrieveAPIView
class FreeCourseRetrieveAPIView(RetrieveAPIView):
    queryset = models.Course.objects.filter(is_delete=False, is_show=True).order_by('-orders').all()
    serializer_class = serializers.FreeCourseModelSerializer


class ChapterListAPIView(ListAPIView):
    queryset = models.CourseChapter.objects.filter(is_delete=False, is_show=True).all()
    serializer_class = serializers.CourseChapterModelSerializer

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['course']







