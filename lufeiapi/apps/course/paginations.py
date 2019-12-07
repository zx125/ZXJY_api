
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class CoursePageNumberPagination(PageNumberPagination):
    # 默认一页条数
    page_size = 2
    # 选择哪一页的key
    page_query_param = 'page'
    # 用户自定义一页条数
    page_size_query_param = 'page_size'
    # 用户自定义一页最大控制条数
    max_page_size = 10

class CourseLimitOffsetPagination(LimitOffsetPagination):
    # 默认一页条数
    default_limit = 2
    # 从offset开始往后显示limit条
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 2


class CourseCursorPagination(CursorPagination):
    cursor_query_param = 'cursor'
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 2
    # ordering = 'id'  # 默认排序规则，不能和排序过滤器OrderingFilter共存