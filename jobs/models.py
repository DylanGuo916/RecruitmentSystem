from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#职位类型
JobTypes = [
    (0, "研发"),
    (1, "运营"),
    (2, "职能/支持"),
    (3, "产品"),
    (4, "设计"),
    (5, "市场"),
    (6, "教研教学"),
    (7, "销售"),
    (8, "游戏策划")
]

#职位城市
Cities = [
    (0, "北京"),
    (1, "上海"),
    (2, "深圳"),
    (3, "杭州"),
    (4, "成都"),
    (5, "广州"),
    (6, "武汉")
]

# 职位要求候选人学历
DEGREE_TYPE = ((u'本科', u'本科'), (u'硕士', u'硕士'), (u'博士', u'博士'))

class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name="职位类别")
    job_name = models.CharField(max_length=250, blank=False, verbose_name="职位名称")
    job_city = models.SmallIntegerField(choices=Cities, blank=False, verbose_name="工作地点")
    job_responsibility = models.TextField(max_length=1024, verbose_name="职位职责")
    job_requirement = models.TextField(max_length=1024, blank=False, verbose_name="职位要求")
    creator = models.ForeignKey(User, verbose_name="创建人", null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name="创建日期", auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name="修改日期", auto_now=True)