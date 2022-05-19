# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from modulos.almacen.models import (
    Variaciones,
    Atributo,
    AtributoValor,
    Producto
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
    list_display = ('codigo', 'nombre', 'descripcion', 'precio_compra', 'precio_venta', 'existencia', 'tipo_producto')
    inlines = [ListVariaciones]


@admin.register(Atributo)
class AtributoAdmin(admin.ModelAdmin):
    inlines = [ListValores]

#admin.site.register(Atributo)
#admin.site.register(AtributoValor)
#admin.site.register(Variaciones)