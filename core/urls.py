from django.conf.urls import url
from .views import api_root, home

urlpatterns = [
    url(r'^root/$', api_root),
    url(r'', home, name='home'),
]
