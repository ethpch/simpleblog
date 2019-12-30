

from django.urls import path
from .views import *


urlpatterns = [
    # User register
    path('register.html', register, name='register'),
    # User login
    path('login.html', userLogin, name='userLogin'),
    # about
    path('about/<int:id>.html', about, name='about'),
]