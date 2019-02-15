# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils import timezone


class Music(models.Model):

    artist = models.CharField(max_length=254, default='')
    song = models.CharField(max_length=254, default='')
    album = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __unicode__(self):
        return self.artist


class Purchase(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='purchases')
    song = models.CharField(max_length=254, default='')
    subscription_end = models.DateTimeField(default=timezone.now)        