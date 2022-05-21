# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from modulos.almacen.models import (
    Variaciones,
    Atributo,
    AtributoValor,
    Producto,
    Categoria,
    Proveedor,
    TipoProducto,
    Sucursal,
    EstadoProducto,
    Serie
)


# Register your models here.
class ListVariaciones(admin.TabularInline):
    model = Variaciones
    extra = 0


class ListValores(admin.TabularInline):
    model = AtributoValor
    extra = 0


@admin.register(Producto)
class ProductosAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'nombre',
        'categoria',
        'descripcion',
        'precio_compra',
        'precio_venta',
        'existencia',
        'existencia_minima',
        'existencia_maxima',
        'tipo_producto'
    )
    inlines = [ListVariaciones]


@admin.register(Atributo)
class AtributoAdmin(admin.ModelAdmin):
    inlines = [ListValores]

@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'estado',
        'proveedor',
        'sucursal',
        'producto',
        'num_serie',
        'ultimo_cambio',
        'comentario',
    )

admin.site.register(Sucursal)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(TipoProducto)
admin.site.register(EstadoProducto)