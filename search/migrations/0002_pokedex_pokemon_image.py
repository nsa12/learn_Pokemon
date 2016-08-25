# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokedex',
            name='pokemon_image',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
