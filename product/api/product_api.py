from django.conf.urls import url
from rest_framework import viewsets
from product.serializers import ProductSerializer
from product.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Product.objects.all()
        return queryset


product_list = ProductViewSet.as_view({'get': 'list', 'post': 'create'})
product_detail = ProductViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }
)

urlpatterns = [
    url(r'^api/v1/products/$', product_list, name="product-list"),
    url(r'^api/v1/products/(?P<pk>[0-9]+)/$', product_detail, name="product-detail"),
]
