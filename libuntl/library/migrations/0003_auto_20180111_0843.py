# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-11 08:43
from __future__ import unicode_literals

from django.db import migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_migrate_from_timordata'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizationtype',
            options={'get_latest_by': 'modified', 'ordering': ('-modified', '-created')},
        ),
        migrations.AddField(
            model_name='organizationtype',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organizationtype',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
    ]
