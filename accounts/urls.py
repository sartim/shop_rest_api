from django.urls import re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.api import fetch_user_api, register_api

urlpatterns = [
    re_path(
        r'^api/v1/account/token-auth', TokenObtainPairView.as_view(),
        name='token_obtain_pair'),
    re_path(
        r'^api/v1/account/token-refresh', TokenRefreshView.as_view(),
        name='token_refresh'),
    re_path(
        r'^api/v1/account/register', register_api.register,
        name='register-user'),
    re_path(
        r'^api/v1/account/user/$', fetch_user_api.fetch_user,
        name='fetch-user'),
]
