# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0013_auto_20180514_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='museo',
            name='numero_comentarios',
            field=models.IntegerField(default=0),
        ),
    ]
