from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from accounts.serializers import UserSerializer


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def register(request):
    if request.method == 'POST':
        user_data = {
            'username': request.data.get('email'),
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'phone': request.data.get('phone'),
            'email': request.data.get('email'),
            'password': request.data.get('password'),
            'confirm_password': request.data.get('confirm_password'),
        }

        serializer = UserSerializer(data=user_data)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
