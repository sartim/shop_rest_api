# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
    label = 'accounts'
    verbose_name = 'Accounts'

    def ready(self):
        from . import signals