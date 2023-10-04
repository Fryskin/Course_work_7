from django.contrib.auth.models import User as DjangoUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User


@receiver(post_save, sender=DjangoUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)
