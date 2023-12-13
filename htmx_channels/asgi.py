import os

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from home.routings import websocket_urlpatterns

from htmx_channels.settings import base_settings

if base_settings.DEBUG:
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "htmx_channels.settings.development_settings"
    )

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "htmx_channels.settings.production_settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
    )
})

app = django_asgi_app