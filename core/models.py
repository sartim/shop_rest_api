# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django_countries.fields import CountryField
from django.utils import timezone


class AbstractDateModel(models.Model):
    """
    Any models that have a created date and updated date should inherit this class
    """
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def save(self, *a, **kw):
        nowtime = timezone.now()
        if self.id is None:
            self.created_date = nowtime
            self.updated_date = nowtime
        self.updated_date = nowtime
        super(AbstractDateModel, self).save(*a, **kw)

    class Meta:
        abstract = True
        ordering = ['-created_date', '-updated_date']


class CityState(models.Model):
    city_state = models.CharField(max_length=255, verbose_name="City / State")
    country = CountryField(blank_label='Select Country')

    class Meta:
        verbose_name_plural = "Cities / States"
        db_table = "cities_states"

    def __str__(self):
        return self.city_state

    def get_absolute_url(self):
        return reverse('job:city-state-detail', kwargs={'pk': self.pk})
