from django.contrib import admin

# Register your models here.


from .models import BlogUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(BlogUser)
class BlogUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'name', 'introduce' , 'company', 'profession', 'address', 'telephone', 'wechat', 'qq', 'weibo', 'photo']
    # add entrance for "mobile", "qq", "wechat" in edit page
    # change type of UserAdmin.fieldsets into list
    fieldsets = list(UserAdmin.fieldsets)
    # rewrite fieldsets, add entrance for model character
    fieldsets[1] = (_('Personal info'),
                    {'fields': ('name', 'introduce', 'email', 'company', 'profession', 'address', 'telephone', 'wechat', 'qq', 'weibo', 'photo')})
    # set data access rights according to current user
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(id=request.user.id)