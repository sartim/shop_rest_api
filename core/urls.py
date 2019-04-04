from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from .views import api_root

schema_view = get_swagger_view(title='API DOC')

urlpatterns = [
    # url(r'', api_root),
    url(r'^$', schema_view)
]
