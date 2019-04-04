from rest_framework import viewsets
from api.serializers import ProductSerializer
from product.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    """
    Products
    """
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Product.objects.all()
        return queryset
