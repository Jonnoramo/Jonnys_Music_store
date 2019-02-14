# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    """
    This is where we define our Post model
    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    category = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    content = models.TextField()
    date = models.DateTimeField(db_index=True, auto_now_add=True)
    views = models.IntegerField(default=0)
    group = models.CharField(max_length=120, blank=True, null=True)
    image = models.ImageField(upload_to="static/images", blank=True, null=True)


    def publish(self):
        self.date = timezone.now()
        self.save()

    def _unicode_(self):
       	   return self.title	

