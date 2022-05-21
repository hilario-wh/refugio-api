# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-05-21 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70, verbose_name='Nombre')),
                ('class_css', models.CharField(max_length=40, verbose_name='Class ccs color')),
                ('para_articulo', models.BooleanField(default=True, verbose_name='Es para Articulo Wifi?')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('color', models.CharField(blank=True, max_length=10, verbose_name='Color para graficar')),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'Estado Articulos',
                'verbose_name_plural': 'Estado Articulos',
            },
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('num_serie', models.CharField(blank=True, max_length=50, verbose_name='N\xb0 Serie')),
                ('ultimo_cambio', models.TextField(blank=True)),
                ('comentario', models.TextField(blank=True, null=True)),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='estado_serie', to='almacen.EstadoProducto', verbose_name='Estado')),
            ],
        ),
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ('-created_at',), 'verbose_name': 'Categoria Producto', 'verbose_name_plural': 'Categoria Productos'},
        ),
        migrations.AlterModelOptions(
            name='proveedor',
            options={'ordering': ('-created_at',), 'verbose_name': 'Proveedor', 'verbose_name_plural': 'Proveedores'},
        ),
        migrations.AlterModelOptions(
            name='sucursal',
            options={'ordering': ('-created_at',), 'verbose_name': 'Sucursal', 'verbose_name_plural': 'Sucursal'},
        ),
        migrations.AlterModelOptions(
            name='tipoproducto',
            options={'ordering': ('-created_at',), 'verbose_name': 'Tipo de producto', 'verbose_name_plural': 'Tipos de producto'},
        ),
        migrations.AddField(
            model_name='producto',
            name='porcentaje_impuesto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Porcentaje de Impuestos'),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='direccion',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Direcci\xf3n'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nombre',
            field=models.CharField(max_length=80, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='representante',
            field=models.CharField(max_length=80, verbose_name='Representante'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefono',
            field=models.CharField(blank=True, max_length=30, verbose_name='Tel\xe9fono'),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='nombre',
            field=models.CharField(max_length=80, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='serie',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serie_producto', to='almacen.Producto', verbose_name='Producto'),
        ),
        migrations.AddField(
            model_name='serie',
            name='proveedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proveedor_serie', to='almacen.Proveedor', verbose_name='Proveedor'),
        ),
        migrations.AddField(
            model_name='serie',
            name='sucursal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sucursal_serie', to='almacen.Sucursal', verbose_name='Sucursal'),
        ),
    ]
