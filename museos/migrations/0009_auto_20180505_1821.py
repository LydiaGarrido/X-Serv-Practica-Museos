# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0008_auto_20180505_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museo',
            name='nombre',
            field=models.TextField(default='Null', max_length=150),
        ),
    ]
