

from django.apps import AppConfig
import os


# change name of app in admin backstage
# value of default_app_config comes form class name of apps.py
default_app_config = 'account.IndexConfig'

# get current app name
def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


# rewrite class IndexConfig
class IndexConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = '用户管理'