# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Museos',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('id_entidad', models.IntegerField(default=0)),
                ('nombre', models.CharField(default='Null', max_length=150)),
                ('horario', models.TextField(default='Null')),
                ('equipamiento', models.TextField(default='Null')),
                ('transporte', models.TextField(default='Null')),
                ('accesibilidad', models.IntegerField(default=0)),
                ('content_url', models.URLField(default='Null', max_length=350)),
                ('nombre_via', models.CharField(default='Null', max_length=50)),
                ('clase_vial', models.CharField(default='Null', max_length=50)),
                ('tipo_num', models.CharField(default='Null', max_length=10)),
                ('num', models.CharField(default='Null', max_length=50)),
                ('localidad', models.CharField(default='Null', max_length=50)),
                ('provincia', models.CharField(default='Null', max_length=50)),
                ('codigo_postal', models.IntegerField(default=0)),
                ('barrio', models.CharField(default='Null', max_length=50)),
                ('distrito', models.CharField(default='Null', max_length=50)),
                ('coordenada_x', models.IntegerField(default=0)),
                ('coordenada_y', models.IntegerField(default=0)),
                ('latitud', models.FloatField(null=True, blank=True)),
                ('longitud', models.FloatField(null=True, blank=True)),
                ('telefono', models.CharField(default='Null', max_length=150)),
                ('fax', models.CharField(default='Null', max_length=100)),
                ('email', models.CharField(default='Null', max_length=100)),
            ],
        ),
    ]
