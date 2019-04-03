from django.conf.urls import url
from accounts.api import fetch_user_api, register_api

urlpatterns = [
    url(r'^api/v1/auth/register/', register_api.register, name='register-user'),
    url(r'^api/v1/auth/user/$', fetch_user_api.fetch_user, name='fetch-user'),
]
