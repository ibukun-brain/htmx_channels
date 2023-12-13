from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import channel_layers
from django.template.loader import get_template


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        # if not self.user.isauthenticated():
        #     self.close()
        #     return
        self.group_name = "notifications"
        await self.channel_layer.group_add(
            self.group_name, self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name, self.channel_name
        )

    async def user_joined(self, event):
        html = get_template("home/partials/notification.html").render(
            context={
                "username": event["text"],
            }
        )
        await self.send(text_data=html)