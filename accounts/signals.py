from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver


# Get the User Model
User = get_user_model()


@receiver(signals.post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Welcome to TSL Wall App!',
            'Hello! Welcome to TSL Wall App!',
            'from@example.com',
            [instance.email],
            fail_silently=False,
        )
