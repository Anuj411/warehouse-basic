"""
ASGI config for e_commers_basic project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
this projected is created by prakash22suthar@gmail.com
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_commers_basic.settings')

application = get_asgi_application()
