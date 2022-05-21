# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Historial(models.Model):
    pass
    # descripcion
    # tipo_movimiento
    # cantidad
    # cantidad_anterior
    # cantidad_actual
    # creado_por
    # actualizado_por
    # creado_en = models.DateTimeField(auto_now_add=True, editable=False)
    # actualizado_en = models.DateTimeField(auto_now_add=True)


class Sucursal(models.Model):
    '''
    Tabla para almacenar sucursales de la empresa
    '''
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    nombre = models.CharField(_('Nombre'), max_length=80)
    #empresa = models.ForeignKey('sistema.Empresa', related_name="empresa_sucursal", on_delete=models.CASCADE)

    # timestamps
    created_at = models.DateTimeField(_('Fecha de creación'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_('Fecha de ultima actualización'), auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Sucursal")
        verbose_name_plural = _("Sucursal")

    def __unicode__(self):
        return self.nombre


class Proveedor(models.Model):
    '''
    Tabla para almacenar proveedores de la empresa
    '''
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    nombre = models.CharField(_('Nombre'), max_length=80)
    email = models.EmailField(_('Email'), blank=True)
    telefono = models.CharField(_('Teléfono'), max_length=30, blank=True)
    direccion = models.CharField(_('Dirección'), max_length=100, null=True, blank=True)
    representante = models.CharField(_('Representante'), max_length=80)
    comentarios = models.TextField(_('Comentarios'), null=True, blank=True)
    #empresa = models.ForeignKey('sistema.Empresa', related_name="empresa_proveedor", on_delete=models.CASCADE)

    # timestamps
    created_at = models.DateTimeField(_('Fecha de creación'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_('Fecha de ultima actualización'), auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Proveedor")
        verbose_name_plural = _("Proveedores")

    def __unicode__(self):
        return self.nombre


class Categoria(models.Model):
    '''
    Tabla para almacenar categorias internas de la empresa (Familias, departamento)
    Ej: Electronicos, Calzado, Consumo
    '''
    nombre = models.CharField(_('Nombre'), max_length=160)
    porcentaje_descuento = models.FloatField(_('Porcentaje de descuento'), max_length=50)
    #empresa = models.ForeignKey('sistema.Empresa', related_name="empresa_categoria", on_delete=models.CASCADE)

    # timestamps
    created_at = models.DateTimeField(_('Fecha de creación'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_('Fecha de ultima actualización'), auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Categoria Producto")
        verbose_name_plural = _("Categoria Productos")

    def __unicode__(self):
        return self.nombre


class TipoProducto(models.Model):
    '''Acceso Staff
    Tipo de producto: Simple, Variable(Deshabilitado), Servicio, Serie
    '''
    nombre = models.CharField(_('Nombre'), max_length=160)

    # timestamps
    created_at = models.DateTimeField(_('Fecha de creación'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_('Fecha de ultima actualización'), auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Tipo de producto")
        verbose_name_plural = _("Tipos de producto")

    def __unicode__(self):
        return self.nombre


class EstadoProducto(models.Model):
    '''Acceso Staff (Derivado de wisphub)
    Estados Wifi: Disponible, Asignado, Dañado, Garantia, Uso Interno
    Estados no Wifi: Eliminado
    '''
    nombre = models.CharField(max_length=70, verbose_name="Nombre")
    class_css = models.CharField(max_length=40, verbose_name="Class ccs color")
    para_articulo = models.BooleanField(default=True, verbose_name="Es para Articulo Wifi?")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    color = models.CharField(max_length=10, verbose_name="Color para graficar", blank=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Estado Articulos"
        verbose_name_plural = "Estado Articulos"

    def __unicode__(self):
        return u'{0}'.format(self.nombre)


class Producto(models.Model):
    '''
    Tabla para almacenar productos Simples, Variables, Servicios, y Sobre los que toma los valores la tabla series
    '''
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_NULL, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True)
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.SET_NULL, null=True, blank=True)
    codigo = models.CharField(_('Codigo'), max_length=50)
    nombre = models.CharField(_('Nombre'), max_length=255)
    descripcion = models.TextField(_('Descripción'))
    marca = models.CharField(_('Marca'), max_length=60)
    modelo = models.CharField(_('Modelo'), max_length=60)
    comentario = models.TextField(_('Comentarios'))
    precio_compra = models.DecimalField(_('Precio de compra'), max_digits=15, decimal_places=2, default=0)
    precio_venta = models.DecimalField(_('Precio de venta'), max_digits=15, decimal_places=2, default=0)
    # Tabla
    # precio_venta_1, precio_venta_2
    # precio_adicional = models.JSONField(_(''), max_length=50) ask: donde guardar los precios adicionales?
    procentaje_comision = models.DecimalField(_('Porcentaje Comisión'), max_digits=15, decimal_places=2, default=0)
    porcentaje_monedero = models.DecimalField(_('Porcentaje Monedero'), max_digits=15, decimal_places=2, default=0)
    porcentaje_descuento = models.DecimalField(_('Porcentaje Descuento'), max_digits=15, decimal_places=2, default=0)
    porcentaje_impuesto = models.DecimalField(_('Porcentaje de Impuestos'), max_digits=15, decimal_places=2, default=0)
    existencia = models.IntegerField(_('Existencia'))
    existencia_maxima = models.IntegerField(_('Inventario Maximo'))
    existencia_minima = models.IntegerField(_('Inventario Minimo'))
    # SAT
    # clave_sat = models.ForeignKey(
    #     'wisp_facturacion.ProductoSAT',
    #     related_name='clave_sat_stock',
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     verbose_name="Clave SAT"
    # )
    # unidad_sat = models.ForeignKey(
    #     'wisp_facturacion.UnidadSAT',
    #     related_name='unidad_sat_stock',
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     verbose_name="Unidad SAT"
    # )
    # empresa = models.ForeignKey('sistema.Empresa', related_name="empresa_producto", on_delete=models.CASCADE)

    # timestamps
    created_at = models.DateTimeField(_('Fecha de creación'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_('Fecha de ultima actualización'), auto_now=True)

    def __unicode__(self):
        return self.nombre


class Serie(models.Model):
    '''
    Tabla para almacenar productos con numero de serie (Renombrada de Articulo en wisphub)
    '''
    producto = models.ForeignKey(
        Producto,
        related_name="serie_producto",
        verbose_name="Producto",
        on_delete=models.CASCADE,
    )
    estado = models.ForeignKey(
        EstadoProducto,
        related_name="estado_serie",
        verbose_name="Estado",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    proveedor = models.ForeignKey(
        Proveedor,
        related_name="proveedor_serie",
        verbose_name="Proveedor",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    sucursal = models.ForeignKey(
        Sucursal,
        related_name="sucursal_serie",
        verbose_name="Sucursal",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    # cliente = models.ForeignKey(
    #     User,
    #     related_name='cliente_articulo',
    #     verbose_name="Cliente",
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True
    # )
    # empresa = models.ForeignKey(
    #     'sistema.Empresa',
    #     related_name="empresa_atributo",
    #     on_delete=models.CASCADE
    # )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    num_serie = models.CharField(max_length=50, verbose_name="N° Serie", blank=True)
    ultimo_cambio = models.TextField(blank=True)
    comentario = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.num_serie



class Atributo(models.Model):
    '''
    Se utiliza para productos variables, son atributos por los que cambia un producto
    Ejemplos: Talla, Color, Serie
    '''
    nombre = models.CharField(_('Nombre'), max_length=50)
    unico = models.BooleanField()
    #empresa = models.ForeignKey('sistema.Empresa', related_name="empresa_atributo", on_delete=models.CASCADE)

    # timestamps
    created_at = models.DateTimeField(_('Fecha de creación'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_('Fecha de ultima actualización'), auto_now=True)


    def __unicode__(self):
        return self.nombre


class AtributoValor(models.Model):
    '''
    Se utiliza para productos variables, son valores para los atributos
    Ejemplos: CH, M, G, XG, Rojo, Verde, Azul
    '''
    atributo = models.ForeignKey(Atributo, on_delete=models.CASCADE)
    nombre = models.CharField(_('Nombre'), max_length=50)
    #empresa = models.ForeignKey('sistema.Empresa', related_name="empresa_atributo_valor", on_delete=models.CASCADE)

    # timestamps
    created_at = models.DateTimeField(_('Fecha de creación'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_('Fecha de ultima actualización'), auto_now=True)

    def __unicode__(self):
        return self.nombre


class Variaciones(models.Model):
    '''
    Se utiliza para productos variables: productos que comparten un mismo codigo de barras
    pero tienen diferentes presentaciones o numeros de serie
    Ejemplos: Playera -> Playera Roja-CH, Playera Azul-G | Tenis -> Tenis Talla 22,23,24
    '''
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    activo = models.BooleanField()
    existencia = models.IntegerField()
    atributos = models.ManyToManyField(AtributoValor)
    #empresa = models.ForeignKey('sistema.Empresa', related_name="empresa_variaciones", on_delete=models.CASCADE)

    # timestamps
    created_at = models.DateTimeField(_('Fecha de creación'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_('Fecha de ultima actualización'), auto_now=True)
