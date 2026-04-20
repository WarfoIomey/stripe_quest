from decimal import Decimal
from dis import disco

from django.db import models
from django.core.validators import MinValueValidator

import payments.constants as constants


class Discount(models.Model):
    """Модель скидки для товаров и заказов."""

    DISCOUNT_TYPE_CHOICES = [
        ('percentage', 'Процент'),
        ('fixed', 'Фиксированная сумма'),
    ]

    name = models.CharField(
        verbose_name='Название скидки',
        help_text='Введите название скидки',
        max_length=constants.MAX_LEN_NAME
    )
    type = models.CharField(
        verbose_name='Тип скидки',
        help_text='Выберите тип скидки',
        max_length=constants.MAX_LEN_TYPE_DISCOUNT,
        choices=DISCOUNT_TYPE_CHOICES
    )
    value = models.DecimalField(
        verbose_name='Значение скидки',
        help_text='Для процентов: число от 0 до 100, для фикс: сумма',
        validators=[MinValueValidator(constants.MIN_VALUE)],
        max_digits=constants.MAX_DIGITS,
        decimal_places=constants.DECIMAL_PLACES
    )
    stripe_coupon_id = models.CharField(
        max_length=constants.MAX_LEN_COUPON_ID,
        blank=True,
        verbose_name='Stripe Coupon ID',
        help_text='Введите ID купона из Stripe'
    )

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return f'{self.name} ({self.type} - {self.value})'


class Tax(models.Model):
    """Модель налога для товаров и заказов."""

    name = models.CharField(
        verbose_name='Название налога',
        help_text='Введите название налога',
        max_length=constants.MAX_LEN_NAME
    )
    percentage = models.DecimalField(
        verbose_name='Процент налога',
        help_text='Введите процент налога (число от 0 до 100)',
        validators=[MinValueValidator(constants.MIN_VALUE)],
        max_digits=constants.MAX_DIGITS,
        decimal_places=constants.DECIMAL_PLACES
    )
    tax_rate_id = models.CharField(
        max_length=constants.MAX_LEN_TAX_ID,
        blank=True,
        verbose_name='Stripe Tax Rate ID',
        help_text='Введите ID налоговой ставки из Stripe'
    )

    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'

    def __str__(self):
        return f'{self.name} ({self.percentage}%)'


class Item(models.Model):
    """Модель товара для оплаты."""

    CURRENCY = [
        ('USD', 'Доллар США'),
        ('EUR', 'Евро'),
        ('RUB', 'Российский рубль'),
    ]

    name = models.CharField(
        verbose_name='Название товара',
        help_text='Введите название товара',
        max_length=constants.MAX_LEN_NAME
    )
    description = models.TextField(
        verbose_name='Описание товара',
        help_text='Введите подробное описание товара'
    )
    price = models.DecimalField(
        verbose_name='Цена товара',
        help_text='Введите цену товара',
        max_digits=constants.MAX_DIGITS,
        decimal_places=constants.DECIMAL_PLACES
    )
    currency = models.CharField(
        verbose_name='Валюта',
        help_text='Выберите валюту (например, USD)',
        max_length=constants.MAX_LEN_CURRENCY,
        choices=CURRENCY
    )
    taxes = models.ManyToManyField(
        Tax,
        blank=True,
        related_name='items',
        verbose_name='Налоги',
        help_text='Выберите налоги для товара',
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name} - {self.price} - {self.currency}'


class Order(models.Model):

    title = models.CharField(
        verbose_name='Название заказа',
        help_text='Введите название заказа',
        max_length=constants.MAX_LEN_NAME
    )
    items = models.ManyToManyField(
        Item,
        related_name='orders',
        verbose_name='Товары в заказе',
        help_text='Выберите товары для заказа',
    )
    discount = models.ForeignKey(
        Discount,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders',
        verbose_name='Скидка',
        help_text='Выберите скидку для заказа',
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_items',
        help_text='Укажите заказ',
        verbose_name='Заказ',
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='order_items',
        help_text='Укажите товары',
        verbose_name='Товар',
    )
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        help_text='Укажите количество',
        verbose_name='Количество'
    )

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'
        unique_together = ['order', 'item']
