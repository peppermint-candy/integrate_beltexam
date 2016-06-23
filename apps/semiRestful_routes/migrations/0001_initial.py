# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 20:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=45)),
                ('product_desc', models.CharField(max_length=255)),
                ('product_pc', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            managers=[
                ('productManager', django.db.models.manager.Manager()),
            ],
        ),
    ]