from django.contrib import admin

# Register your models here.


from .models import *
admin.site.site_title = '博客管理后台'
admin.site.site_header = '博客管理'


@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag', 'user']
    # set data access rights according to current user
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user_id=request.user.id)
    # set foreign key when add or modify data
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user':
            id = request.user.id
            kwargs["queryset"] = BlogUser.objects.filter(id=id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(ArticleInfo)
class ArticleInfoAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'content', 'articlephoto', 'created', 'updated']
    # set data access rights according to current user
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(author_id=request.user.id)
    # set foreign key when add or modify data
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'article_tag':
            id = request.user.id
            kwargs["queryset"] = ArticleTag.objects.filter(user_id=id)
        return super().formfield_for_manytomany(db_field, request, **kwargs)
    # set foreign key when add or modify data
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            id = request.user.id
            kwargs["queryset"] = BlogUser.objects.filter(id=id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['article', 'commentator', 'content', 'created']
    # set data access rights according to current user
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(article__author__id=request.user.id)
    # set foreign key when add or modify data
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'article':
            id = request.user.id
            kwargs["queryset"] = Comment.objects.filter(article__author__id=id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)