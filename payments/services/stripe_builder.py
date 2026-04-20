from decimal import Decimal


class StripeItemBuilder:

    @staticmethod
    def line_from_item(item, quantity=1):
        data = {
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': int(Decimal(item.price) * 100),
            },
            'quantity': quantity,
        }
        if item.taxes.exists():
            data['tax_rates'] = [tax.tax_rate_id for tax in item.taxes.all()]
        return data

    @classmethod
    def line_from_order(cls, order):
        return [
            cls.line_from_item(order_item.item, order_item.quantity)
            for order_item in order.order_items.select_related('item')
        ]