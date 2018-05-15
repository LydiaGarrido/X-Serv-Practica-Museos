# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0014_museo_numero_comentarios'),
    ]

    operations = [
        migrations.RenameField(
            model_name='museo',
            old_name='numero_comentarios',
            new_name='num_coment',
        ),
    ]
