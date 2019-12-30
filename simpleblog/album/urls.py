

from django.urls import path
from .views import *


urlpatterns = [
    # album
    path('<int:id>/<int:page>.html', album, name='album'),
]