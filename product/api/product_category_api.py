from django.conf.urls import url
from rest_framework import viewsets
from product.category.serializers import CategorySerializer
from product.category.models import ProductCategory


class ProductCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self, *args, **kwargs):
        queryset = ProductCategory.objects.all()
        return queryset


category_list = ProductCategoryViewSet.as_view({'get': 'list', 'post': 'create'})
category_detail = ProductCategoryViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                  'patch': 'partial_update',
                                                  'delete': 'destroy'})

urlpatterns = [
    url(r'^api/v1/category/$', category_list, name="category-list"),
    url(r'^api/v1/category/(?P<pk>[0-9]+)/$', category_detail, name="category-detail"),
]
