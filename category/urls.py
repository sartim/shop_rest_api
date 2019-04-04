from django.conf.urls import url

from category.views import CategoryViewSet

category_list = CategoryViewSet.as_view({'get': 'list', 'post': 'create'})
category_detail = CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update',
                                           'delete': 'destroy'})

urlpatterns = [
    url(r'^api/v1/category/$', category_list, name="category-list"),
    url(r'^api/v1/category/(?P<pk>[0-9]+)/$', category_detail, name="category-detail"),
]
