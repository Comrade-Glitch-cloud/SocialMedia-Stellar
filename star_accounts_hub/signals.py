from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import CadetProfile

@receiver(post_save, sender=User)
def create_or_update_cadetprofile(sender, instance, created, **kwargs):
    if created:
        CadetProfile.objects.create(user=instance)
    instance.cadet.save()
