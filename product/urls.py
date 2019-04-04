from django.conf.urls import url
from product.views import ProductViewSet

product_list = ProductViewSet.as_view({'get': 'list', 'post': 'create'})
product_detail = ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update',
                                         'delete': 'destroy'})

urlpatterns = [
    url(r'^api/v1/product/$', product_list, name="product-list"),
    url(r'^api/v1/product/(?P<pk>[0-9]+)/$', product_detail, name="product-detail"),
]
