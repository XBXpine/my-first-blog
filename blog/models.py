from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

# 定义Post模型，用于存储文章信息
class Post(models.Model):
    # 定义外键，用于关联用户表
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 定义标题字段，最大长度为200
    title = models.CharField(max_length=200)
    # 定义文本字段，最大长度为500
    text = models.TextField()
    # 定义创建时间字段，默认值为当前时间
    created_date = models.DateTimeField(default=timezone.now)
    # 定义发布时间字段，可以为空
    published_date = models.DateTimeField(blank=True, null=True)

    # 定义发布方法，将发布时间字段设置为当前时间，并保存
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # 定义字符串方法，返回标题
    def __str__(self):
        return self.title
