# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def add_actors(apps, schema_editor):
    Actor = apps.get_model('foo', 'Actor')
    jean_actor = Actor.objects.filter(name='Jean')
    if not jean_actor:
        Actor.objects.create(name='Jean')

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.RunPython(add_actors),
    ]
