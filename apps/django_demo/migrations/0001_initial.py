# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-08 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('new_login', '0002_user_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('travel_date_from', models.DateTimeField()),
                ('travel_date_to', models.DateTimeField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_by', to='new_login.User')),
                ('joined_trip', models.ManyToManyField(related_name='joined_trip', to='new_login.User')),
            ],
        ),
    ]
