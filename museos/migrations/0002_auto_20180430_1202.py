# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('museos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(default='Null')),
            ],
        ),
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, default='Null')),
                ('letra_size', models.CharField(max_length=50, default='Null')),
                ('color_fondo', models.CharField(max_length=50, default='Null')),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seleccion',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Museos',
            new_name='Museo',
        ),
        migrations.AddField(
            model_name='seleccion',
            name='museo',
            field=models.ForeignKey(to='museos.Museo'),
        ),
        migrations.AddField(
            model_name='seleccion',
            name='usario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comentarios',
            name='museo',
            field=models.ForeignKey(to='museos.Museo'),
        ),
    ]
