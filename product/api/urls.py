from django.conf.urls import url
from django.urls import include

urlpatterns = [
    url(r'', include('product.api.product_api')),
    url(r'', include('product.api.product_category_api'))
]