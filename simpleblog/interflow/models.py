from django.db import models

# Create your models here.


from account.models import BlogUser
from django.utils import timezone


class Board(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('留言用户', max_length=50)
    email = models.CharField('邮箱地址', max_length=50)
    content = models.CharField('留言内容', max_length=500)
    created = models.DateTimeField('创建时间', default=timezone.now)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE, verbose_name='用户')

    def __str__(self):
        return self.email


    class Meta:
        verbose_name = '博客留言'
        verbose_name_plural = '博客留言'