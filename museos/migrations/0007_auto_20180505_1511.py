# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0006_auto_20180504_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museo',
            name='id_entidad',
            field=models.CharField(default='Null', max_length=150),
        ),
    ]
