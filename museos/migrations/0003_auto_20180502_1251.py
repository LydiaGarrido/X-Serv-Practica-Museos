# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0002_auto_20180430_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='museo',
            name='descripcion',
            field=models.TextField(default='Null'),
        ),
        migrations.AddField(
            model_name='museo',
            name='descripcion_entidad',
            field=models.TextField(default='Null'),
        ),
        migrations.AddField(
            model_name='museo',
            name='orientacion',
            field=models.TextField(default='Null'),
        ),
        migrations.AddField(
            model_name='museo',
            name='planta',
            field=models.CharField(max_length=50, default='Null'),
        ),
    ]
