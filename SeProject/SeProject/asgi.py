"""
ASGI config for SeProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import DiscussionApp.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SeProject.settings')

application = ProtocolTypeRouter({
  'https': get_asgi_application(),
  'websocket': AuthMiddlewareStack(DiscussionApp.routing.websocketURLPatterns)
})
django.setup()

application = get_asgi_application()
