

from django.urls import path
from django.views.generic import RedirectView
from .views import *


urlpatterns = [
    # index page turn to user login page
    path('', RedirectView.as_view(url='user/login.html')),
    # article list
    path('<int:id>/<int:page>.html', article, name='article'),
    # article text
    path('detail/<int:id>/<int:aId>.html', detail, name='detail'),
]