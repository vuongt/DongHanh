# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-04 22:34
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
            name='University',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='University Name')),
                ('short_name', models.CharField(max_length=10, unique=True, verbose_name='University short name')),
                ('slug', models.SlugField(max_length=60, unique=True)),
                ('about', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created_on')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]