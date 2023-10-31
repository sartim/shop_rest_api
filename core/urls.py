from django.urls import re_path
from .views import api_root, home

urlpatterns = [
    re_path(r'^root/$', api_root),
    re_path(r'^$', home, name='home'),
]
