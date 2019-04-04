# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from accounts.serializers import UserSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }


@api_view(['GET'])
def api_root(request, format=None):
    """
    API Root
    :param request:
    :param format:
    :return: Response
    """
    return Response({
        # 'category-list': reverse('category-list', request=request, format=format),
    })


@api_view(['GET'])
@permission_classes([])
def home(request, format=None):
    """
    Home
    :param request:
    :param format:
    :return: Response
    """
    return Response("Welcome!")
