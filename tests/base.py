import os
import dotenv
from django.core.wsgi import get_wsgi_application

dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
application = get_wsgi_application()

from rest_framework.test import APIClient


class Base:
    @classmethod
    def setup_class(cls):
        cls.client = APIClient()
        cls.product_url = '/api/v1/product/'
        cls.user_url = '/api/v1/account/user/'
        cls.category_url = '/api/v1/category/'
        cls.order_url = '/api/v1/order/'
        os.system('python manage.py migrate')
        os.system('python manage.py add_product_data')

    @classmethod
    def teardown_class(cls):
        os.system('rm test.sqlite3')
