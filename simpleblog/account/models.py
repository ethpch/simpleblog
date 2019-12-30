from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser


class BlogUser(AbstractUser):
    name = models.CharField('姓名', max_length=50, default='匿名用户')
    introduce = models.TextField('简介', default='暂无介绍')
    company = models.CharField('公司', max_length=100, default='暂无介绍')
    profession = models.CharField('职业', max_length=100, default='暂无介绍')
    address = models.CharField('地址', max_length=100, default='暂无信息')
    telephone = models.CharField('电话', max_length=11, default='暂无信息')
    wechat = models.CharField('微信', max_length=30, default='暂无信息')
    qq = models.CharField('QQ', max_length=30, default='暂无信息')
    weibo = models.CharField('微博', max_length=50, default='暂无信息')
    photo = models.ImageField('头像', blank=True, upload_to='images/user/')

    def __str__(self):
        return self.name