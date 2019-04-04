# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from core.models import AbstractDateModel


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create and return a `User` with an email, and password."""

        if email is None:
            raise TypeError('Users must have an email address.')

        """ Take out username from extra_fields """

        user = self.model(
            username=self.normalize_email(email),
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

    def phone_is_unique(self, phone):
        return not super(UserManager, self).filter(phone=phone).exists()


class User(AbstractBaseUser, PermissionsMixin, AbstractDateModel):
    email = models.CharField(max_length=128, unique=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    original_referrer = models.CharField(max_length=255, blank=True, null=True)
    invite_code = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    login_token = models.CharField(max_length=255, blank=True, null=True)

    # The `USERNAME_FIELD` property tells us which field we will use to log in.
    # In this case, we want that to be the email field.
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['phone']

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        if self.first_name:
            return self.get_full_name()
        return self.email

    def get_short_name(self):
        return '{}'.format(self.first_name)

    def get_full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    @property
    def is_admin(self):
        if self.is_superuser or self.is_staff:
            return True
        return False

    @property
    def total_applied_count(self):
        return self.applications.count()

    @property
    def applications_count(self):
        if self.total_applied_count:
            return self.total_applied_count % 5
        else:
            return 0

    @property
    def is_first_time(self):
        if self.applications_count > 0:
            return False
        return True


class LoggedInUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='logged_in_user', on_delete=models.CASCADE)
