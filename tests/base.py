import os
import random

from django.test import TestCase
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

load_dotenv()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
application = get_wsgi_application()

from rest_framework_simplejwt.tokens import AccessToken
from accounts.models import User


class Base(TestCase):
    @classmethod
    def setup_class(cls):
        cls.token_auth_url = '/api/v1/account/token-auth'
        cls.product_url = '/api/v1/products/'
        cls.user_url = '/api/v1/account/users/'
        cls.category_url = '/api/v1/categories/'
        cls.order_url = '/api/v1/orders/'

        os.system('python manage.py migrate')
        os.system('python manage.py add_product_data')

        random_int = random.randint(0, 100)
        cls.email = 'test{}@mail.com'.format(random_int)
        cls.password = 'test123'

        user = User.objects.create_superuser(cls.email, cls.password)
        cls.token = AccessToken.for_user(user)

    @classmethod
    def teardown_class(cls):
        os.system('rm -f test.sqlite3')
