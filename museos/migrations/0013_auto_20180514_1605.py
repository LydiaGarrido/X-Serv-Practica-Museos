# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0012_auto_20180514_0826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seleccion',
            old_name='usario',
            new_name='usuario',
        ),
    ]
