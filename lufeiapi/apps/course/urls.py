from django.urls import path, re_path

from . import views
urlpatterns = [
    path('free', views.FreeCourseListAPIView.as_view()),
    re_path('^free/(?P<pk>\d+)$', views.FreeCourseRetrieveAPIView.as_view()),
    path('categories', views.CategoryListAPIView.as_view()),
    path('chapters', views.ChapterListAPIView.as_view()),
]