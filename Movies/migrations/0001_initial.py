# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default=None, max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=255, null=True, blank=True)),
                ('director', models.CharField(default=None, max_length=255, null=True, blank=True)),
                ('popularity', models.FloatField(null=True, blank=True)),
                ('imdb_score', models.FloatField(null=True, blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('genre', models.ManyToManyField(to='Movies.Genre')),
            ],
        ),
    ]
