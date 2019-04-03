from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def fetch_user(request):
    data = None
    if request.method == 'GET':
        data = {
            'user_id': request.user.id,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.username,
            'is_active': request.user.is_active
        }
    return Response(data)
