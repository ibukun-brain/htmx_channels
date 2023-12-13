import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

from htmx_channels.settings import base_settings

if base_settings.DEBUG:
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE", "htmx_channels.settings.development_settings"
        )

# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    # Just HTTP for now. (We can add other protocols later.)
})

app = application