import os
import django
import dotenv

from channels.routing import get_default_application

dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()
application = get_default_application()
