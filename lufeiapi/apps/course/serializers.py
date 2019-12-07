
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
            # 'course_category'
        )

class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ('id', 'name')

class CourseSectionModelSerializer(ModelSerializer):
    class Meta:
        model = models.CourseSection
        fields = '__all__'

class CourseChapterModelSerializer(ModelSerializer):
    coursesections = CourseSectionModelSerializer(many=True)
    class Meta:
        model = models.CourseChapter
        fields = (
            'id',
            'name',
            'chapter',
            'summary',
            'coursesections',
        )



