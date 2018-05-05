# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0005_auto_20180504_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museo',
            name='coordenada_x',
            field=models.CharField(max_length=50, default='Null'),
        ),
        migrations.AlterField(
            model_name='museo',
            name='coordenada_y',
            field=models.CharField(max_length=50, default='Null'),
        ),
        migrations.AlterField(
            model_name='museo',
            name='latitud',
            field=models.CharField(max_length=50, default='Null'),
        ),
        migrations.AlterField(
            model_name='museo',
            name='longitud',
            field=models.CharField(max_length=50, default='Null'),
        ),
    ]
