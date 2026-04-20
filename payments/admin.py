from django.contrib import admin

from .models import Item, Order, OrderItem, Discount, Tax


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    """Кастомная админка для модели Discount."""

    list_display = (
        'id',
        'name',
        'stripe_coupon_id',
        'type',
        'value',
    )
    search_fields = ('name', 'stripe_coupon_id', 'value')
    list_filter = ('type',)


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    """Кастомная админка для модели Tax."""

    list_display = (
        'id',
        'name',
        'tax_rate_id',
        'percentage',
    )
    search_fields = ('name', 'tax_rate_id', 'percentage')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Кастомная админка для модели Item."""

    list_display = (
        'id',
        'name',
        'description',
        'price',
        'currency',
    )
    list_filter = ('name', 'currency')
    search_fields = ('name', 'description', 'price')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Кастомная админка для модели Order."""

    list_display = (
        'id',
        'title',
    )
    search_fields = ('title',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """Кастомная админка для модели OrderItem."""

    list_display = (
        'id',
        'order',
        'item',
        'quantity',
    )
    search_fields = ('order__id', 'item__name')
    list_filter = ('order', 'item')
