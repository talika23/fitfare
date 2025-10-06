
import os
from channels.routing import get_default_application
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitfare_project.settings')

django_asgi_app = get_asgi_application()
application = get_default_application()
