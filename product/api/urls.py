from django.urls import include, re_path

urlpatterns = [
    re_path(r'', include('product.api.product_api')),
    re_path(r'', include('product.api.product_category_api'))
]
