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
        os.system('python manage.py migrate')

    @classmethod
    def teardown_class(cls):
        os.system('rm test.sqlite3')
