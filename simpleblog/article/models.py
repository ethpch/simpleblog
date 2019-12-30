from django.db import models

# Create your models here.


from django.utils import timezone
from account.models import BlogUser
# import character type defined by editor
from ckeditor_uploader.fields import RichTextUploadingField


class ArticleTag(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField('标签', max_length=200)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE, verbose_name='用户')

    def __str__(self):
        return self.tag


    class Meta:
        verbose_name = '博文分类'
        verbose_name_plural = '博文分类'


class ArticleInfo(models.Model):
    author = models.ForeignKey(BlogUser, on_delete=models.CASCADE, verbose_name='用户')
    title = models.CharField('标题', max_length=200)
    content = RichTextUploadingField('内容')
    articlephoto = models.ImageField('文章图片', blank=True, upload_to='images/article/')
    reading = models.IntegerField('阅读量', default=0)
    liking = models.IntegerField('点赞量', default=0)
    created = models.DateTimeField('创建时间', default=timezone.now)
    updated = models.DateTimeField('更新时间', auto_now=True)
    article_tag = models.ManyToManyField(ArticleTag, blank=True, verbose_name='文章标签')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = '博文管理'
        verbose_name_plural = '博文管理'


class Comment(models.Model):
    article = models.ForeignKey(ArticleInfo, on_delete=models.CASCADE, verbose_name='所属文章')
    commentator = models.CharField('评论用户', max_length=50)
    content = models.TextField('评论内容')
    created = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.article.title


    class Meta:
        verbose_name = '评论管理'
        verbose_name_plural = '评论管理'