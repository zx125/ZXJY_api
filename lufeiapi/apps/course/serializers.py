from rest_framework.serializers import ModelSerializer
from . import models

class TeacherModelSerializer(ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = (
            'name',
            'role_name',
            'title',
            'signature',
            'image',
            'brief',
        )

class FreeCourseModelSerializer(ModelSerializer):
    teacher = TeacherModelSerializer()
    class Meta:
        model = models.Course
        fields = (
            'id',
            'name',
            'course_img',
            'brief',
            'level_name',
            'period',
            'students',
            'sections',
            'price',
            'teacher',
            'section_list',
        )