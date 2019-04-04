from rest_framework import viewsets
from api.models import Category
from category.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Categories
    """
    serializer_class = CategorySerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Category.objects.all()
        return queryset
