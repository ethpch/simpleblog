

from django.urls import path
from .views import *


urlpatterns = [
    # Board
    path('<int:id>/<int:page>.html', board, name='board'),
]