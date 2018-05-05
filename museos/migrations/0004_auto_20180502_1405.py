# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0003_auto_20180502_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='comentario',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='color_fondo',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='letra_size',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='titulo',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='museo',
            name='barrio',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AlterField(
            model_name='museo',
            name='clase_vial',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AlterField(
            model_name='museo',
            name='content_url',
            field=models.URLField(max_length=350, default=''),
        ),
        migrations.AlterField(
            model_name='museo',
            name='descripcion',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='museo',
            name='descripcion_entidad',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='museo',
            name='distrito',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AlterField(
            model_name='museo',
            name='email',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='museo',
            name='equipamiento',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='museo',
            name='fax',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='museo',
            name='horario',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='museo',
            name='localidad',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AlterField(
            model_name='museo',
            name='nombre',
            field=models.CharField(max_length=150, default=''),
        ),
        migrations.AlterField(
            model_name='museo',
            name='nombre_via',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AlterField(
            model_name='museo',
            name='num',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AlterField(
            model_name='museo',
            name='orientacion',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='museo',
            name='planta',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AlterField(
            model_name='museo',
            name='provincia',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AlterField(
            model_name='museo',
            name='telefono',
            field=models.CharField(max_length=150, default=''),
        ),
        migrations.AlterField(
            model_name='museo',
            name='tipo_num',
            field=models.CharField(max_length=10, default=''),
        ),
        migrations.AlterField(
            model_name='museo',
            name='transporte',
            field=models.TextField(default=''),
        ),
    ]
