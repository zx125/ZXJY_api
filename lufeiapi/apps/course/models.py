from django.db import models

"""
class Course(models.Model):
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    students = models.IntegerField(default=0)
    level = models.IntegerField(choices=((0, '入门'), (1, '进阶')), default=0)
    time = models.IntegerField(default=0)
    detail = models.TextField()  # 可以关联详情表
    type = models.IntegerField(choices=((0, 'Python'), (1, 'Linux')), default=0)
    is_show = models.BooleanField(default=False)

    class Meta:
        abstract = True

# 免费课
class FreeCourse(Course):
    image = models.ImageField(upload_to='course/free')
    attachment = models.FileField(upload_to='attachment')

# 实战课
class ActualCourse():
    image = models.ImageField(upload_to='course/actual')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    cost = models.DecimalField(max_digits=7, decimal_places=2)

# 轻课
class LightCourse():
    image = models.ImageField(upload_to='course/light')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    period = models.IntegerField(verbose_name='学习建议周期(month)', default=0)

# 评论表：分三个表、(id，ctx，date，user_id，free_course_id, comment_id)
# 老师表：在课程表建立多对一外键
# 章节表：在章节表建立多对一外键关联课程
# 课时表：在课时表建立多对一外键关联章节
"""


from utils.model import BaseModel

class CourseCategory(BaseModel):
    """分类"""
    name = models.CharField(max_length=64, unique=True, verbose_name="分类名称")
    orders = models.IntegerField(default=0)
    class Meta:
        db_table = "luffy_course_category"
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name


class Course(BaseModel):
    """课程"""
    course_type = (
        (0, '付费'),
        (1, 'VIP专享'),
        (2, '学位课程')
    )
    level_choices = (
        (0, '初级'),
        (1, '中级'),
        (2, '高级'),
    )
    status_choices = (
        (0, '上线'),
        (1, '下线'),
        (2, '预上线'),
    )
    name = models.CharField(max_length=128, verbose_name="课程名称")
    course_img = models.ImageField(upload_to="courses", max_length=255, verbose_name="封面图片", blank=True, null=True)
    course_type = models.SmallIntegerField(choices=course_type, default=0, verbose_name="付费类型")
    # 使用这个字段的原因
    brief = models.TextField(max_length=2048, verbose_name="详情介绍", null=True, blank=True)
    level = models.SmallIntegerField(choices=level_choices, default=0, verbose_name="难度等级")
    pub_date = models.DateField(verbose_name="发布日期", auto_now_add=True)
    period = models.IntegerField(verbose_name="建议学习周期(day)", default=7)
    attachment_path = models.FileField(upload_to="attachment", max_length=128, verbose_name="课件路径", blank=True,
                                       null=True)
    status = models.SmallIntegerField(choices=status_choices, default=0, verbose_name="课程状态")
    course_category = models.ForeignKey("CourseCategory", on_delete=models.SET_NULL, db_constraint=False, null=True, blank=True,
                                        verbose_name="课程分类")
    students = models.IntegerField(verbose_name="学习人数", default=0)
    sections = models.IntegerField(verbose_name="总课时数量", default=0)
    pub_sections = models.IntegerField(verbose_name="课时更新数量", default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="课程原价", default=0)
    teacher = models.ForeignKey("Teacher", on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="授课老师")
    orders = models.IntegerField(default=0)

    @property
    def level_name(self):
        return self.get_level_display()

    @property
    def section_list(self):
        temp_section_list = []
        for chapter in self.coursechapters.all():
            for section in chapter.coursesections.all():
                if len(temp_section_list) >= 4:
                    return temp_section_list
                temp_section_list.append({
                    'chapter': chapter.chapter,
                    'name': section.name,
                    'free_trail': section.free_trail,
                })
        return temp_section_list

    class Meta:
        db_table = "luffy_course"
        verbose_name = "课程"
        verbose_name_plural = "课程"

    def __str__(self):
        return "%s" % self.name


class Teacher(BaseModel):
    """导师"""
    role_choices = (
        (0, '讲师'),
        (1, '导师'),
        (2, '班主任'),
    )
    name = models.CharField(max_length=32, verbose_name="导师名")
    role = models.SmallIntegerField(choices=role_choices, default=0, verbose_name="导师身份")
    title = models.CharField(max_length=64, verbose_name="职位、职称")
    signature = models.CharField(max_length=255, verbose_name="导师签名", help_text="导师签名", blank=True, null=True)
    image = models.ImageField(upload_to="teacher", null=True, verbose_name="导师封面")
    brief = models.TextField(max_length=1024, verbose_name="导师描述")
    orders = models.IntegerField(default=0)

    @property
    def role_name(self):
        return self.get_role_display()

    class Meta:
        db_table = "luffy_teacher"
        verbose_name = "导师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name


class CourseChapter(BaseModel):
    """章节"""
    course = models.ForeignKey("Course", related_name='coursechapters', on_delete=models.CASCADE, verbose_name="课程名称")
    chapter = models.SmallIntegerField(verbose_name="第几章", default=1)
    name = models.CharField(max_length=128, verbose_name="章节标题")
    summary = models.TextField(verbose_name="章节介绍", blank=True, null=True)
    pub_date = models.DateField(verbose_name="发布日期", auto_now_add=True)
    orders = models.IntegerField(default=0)

    class Meta:
        db_table = "luffy_course_chapter"
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s:(第%s章)%s" % (self.course, self.chapter, self.name)


class CourseSection(BaseModel):
    """课时"""
    section_type_choices = (
        (0, '文档'),
        (1, '练习'),
        (2, '视频')
    )
    chapter = models.ForeignKey("CourseChapter", related_name='coursesections', on_delete=models.CASCADE,
                                verbose_name="课程章节")
    name = models.CharField(max_length=128, verbose_name="课时标题")
    orders = models.PositiveSmallIntegerField(verbose_name="课时排序")
    section_type = models.SmallIntegerField(default=2, choices=section_type_choices, verbose_name="课时种类")
    section_link = models.CharField(max_length=255, blank=True, null=True, verbose_name="课时链接",
                                    help_text="若是video，填vid,若是文档，填link")
    duration = models.CharField(verbose_name="视频时长", blank=True, null=True, max_length=32)  # 仅在前端展示使用
    pub_date = models.DateTimeField(verbose_name="发布时间", auto_now_add=True)
    free_trail = models.BooleanField(verbose_name="是否可试看", default=False)


    class Meta:
        db_table = "luffy_course_Section"
        verbose_name = "课时"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s-%s" % (self.chapter, self.name)
