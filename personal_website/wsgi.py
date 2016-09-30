import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
"""
WSGI config for my personal website.
"""

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personal_website.settings")
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
