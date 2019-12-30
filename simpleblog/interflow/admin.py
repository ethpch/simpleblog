from django.contrib import admin

# Register your models here.


from .models import Board
from account.models import BlogUser


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'content', 'created', 'user']
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