"""
ASGI config for email_auth project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from user_app.api import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_auth.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(AuthMiddlewareStack(
        URLRouter(routing.ASGI_urlpatterns)
        ))
})

