from django.shortcuts import render
from rest_framework.generics import ListAPIView
# Create your views here.
from . import models,serializers

class FreeCourseListAPIView(ListAPIView):
    queryset = models.Course.objects.filter(is_delete=False, is_show=True).order_by('-orders').all()
    serializer_class = serializers.FreeCourseModelSerializer