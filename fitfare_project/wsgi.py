import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitfare_project.settings')

application = get_wsgi_application()  # must be named exactly 'application'
