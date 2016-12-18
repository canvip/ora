# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-15 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firset_name', models.CharField(blank=True, max_length=120, null=True)),
                ('last_name', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('times_temp', models.DateTimeField(auto_now_add=True)),
                ('updatad', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
