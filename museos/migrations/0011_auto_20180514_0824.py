# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0010_auto_20180505_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museo',
            name='nombre',
            field=models.CharField(default='Null', max_length=150),
        ),
    ]
