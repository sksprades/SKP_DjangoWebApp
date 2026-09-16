"""
WSGI config for SKP_DjangoWebApp project.
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SKP_DjangoWebApp.settings')

application = get_wsgi_application()
