# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-12 14:57
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', django.contrib.postgres.fields.jsonb.JSONField(blank=True, max_length=128, null=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('cover', models.ImageField(blank=True, max_length=200, null=True, upload_to='')),
                ('language', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('file', models.FileField(blank=True, max_length=200, null=True, upload_to='')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.TextField()),
                ('acronyms', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('description', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('contact', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganizationType',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('name', django.contrib.postgres.fields.jsonb.JSONField()),
                ('description', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PublicationType',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('name', django.contrib.postgres.fields.jsonb.JSONField()),
                ('description', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Publication Types',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Year')),
                ('name', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='name')),
                ('description', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='description')),
                ('cover', models.ImageField(blank=True, max_length=200, null=True, upload_to='')),
                ('author', models.ManyToManyField(blank=True, to='library.Author')),
                ('organization', models.ManyToManyField(blank=True, to='library.Organization')),
                ('pubtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.PublicationType', verbose_name='Type')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', django.contrib.postgres.fields.jsonb.JSONField()),
                ('description', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='resource',
            name='tag',
            field=models.ManyToManyField(blank=True, to='library.Tag'),
        ),
        migrations.AddField(
            model_name='resource',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='organization',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.OrganizationType', verbose_name='Organization Type'),
        ),
        migrations.AddField(
            model_name='link',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Resource'),
        ),
    ]
