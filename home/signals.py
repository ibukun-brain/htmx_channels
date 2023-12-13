from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

User = get_user_model()

@receiver(post_save, sender=User)
def send_notification_on_signup(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        group = "notifications"
        event = {
            "type": "user.joined",
            "text": instance.username,
        }
        async_to_sync(channel_layer.group_send)(group, event)