from django.db import models

import payments.constants as constants


class Item(models.Model):
    """Модель товара для оплаты."""

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
        max_digits=constants.MAX_DIGITS_PRICE,
        decimal_places=constants.DECIMAL_PLACES_PRICE
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name} - {self.price}'
