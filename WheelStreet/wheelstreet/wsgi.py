"""
WSGI config for wheelstreet project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

print("Current working directory:", os.getcwd())  # Debugging line
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wheelstreet.settings')
application = get_wsgi_application()
