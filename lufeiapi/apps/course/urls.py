from django.urls import path, re_path

from . import views
urlpatterns = [
    path('free', views.FreeCourseListAPIView.as_view()),
]