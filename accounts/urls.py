from django.conf.urls import url
from rest_framework_jwt.views import (
    obtain_jwt_token, refresh_jwt_token, verify_jwt_token)
from accounts.api import fetch_user_api, register_api

urlpatterns = [
    url(r'^api/v1/account/token-auth', obtain_jwt_token),
    url(r'^api/v1/account/token-refresh', refresh_jwt_token),
    url(r'^api/v1/account/token-verify', verify_jwt_token),
    url(r'^api/v1/account/register', register_api.register, name='register-user'),
    url(r'^api/v1/account/user/$', fetch_user_api.fetch_user, name='fetch-user'),
]
