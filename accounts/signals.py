from __future__ import unicode_literals

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import user_logged_in, user_logged_out
from .models import User, LoggedInUser


@receiver(pre_save, sender=User)
def user_pre_save(sender, instance, **kwargs):
    pass

@receiver(user_logged_in)
def on_user_login(sender, **kwargs):
    LoggedInUser.objects.get_or_create(user=kwargs.get('user'))


@receiver(user_logged_out)
def on_user_logout(sender, **kwargs):
    LoggedInUser.objects.filter(user=kwargs.get('user')).delete()
