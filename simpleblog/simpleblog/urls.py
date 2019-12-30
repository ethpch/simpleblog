"""
Definition of urls for simpleblog.
"""

from django.urls import path, include, re_path
from django.contrib import admin
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    # Admin backstage
    path('admin/', admin.site.urls),
    # user register and login
    path('user/', include('account.urls')),
    # blog article
    path('', include('article.urls')),
    # album
    path('album/', include('album.urls')),
    # board
    path('board/', include('interflow.urls')),
    # set router of media resource
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    # set router of static resource
    re_path('static/(?P<path>.*)', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    # set router path of editor
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
