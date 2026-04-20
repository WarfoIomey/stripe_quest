from django.urls import reverse

from ..stripe_client import stripe
from .stripe_builder import StripeItemBuilder


class StripeService:

    @staticmethod
    def create_order_session(order, request):
        session_data = {
            'payment_method_types': ['card'],
            'line_items': StripeItemBuilder.line_from_order(order),
            'mode': 'payment',
            'success_url': request.build_absolute_uri(reverse(
                'payments:success'
            )),
            'cancel_url': request.build_absolute_uri(
                reverse('payments:cancel')
            ),
        }
        if order.discount:
            session_data['discounts'] = [{
                'coupon': order.discount.stripe_coupon_id
            }]
        return stripe.checkout.Session.create(**session_data)

    @staticmethod
    def create_item_session(item, request):
        session_data = {
            'payment_method_types': ['card'],
            'line_items': [StripeItemBuilder.line_from_item(item)],
            'mode': 'payment',
            'success_url': request.build_absolute_uri(
                reverse('payments:success')
                ),
            'cancel_url': request.build_absolute_uri(
                reverse('payments:cancel')
            ),
        }
        return stripe.checkout.Session.create(**session_data)
