# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-14 22:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('views', models.IntegerField(default=0)),
                ('group', models.CharField(blank=True, max_length=120, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
