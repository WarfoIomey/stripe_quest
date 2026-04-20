from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.conf import settings

from .services.stripe_service import StripeService
from .mixins import StripeCheckoutMixin
from .models import Item, Order


class BuyOrderView(StripeCheckoutMixin, DetailView):
    model = Order
    pk_url_kwarg = 'order_id'

    def get_stripe_session(self, obj, request):
        return StripeService.create_order_session(obj, request)


class BuyItemView(StripeCheckoutMixin, DetailView):
    model = Item
    pk_url_kwarg = 'item_id'

    def get_stripe_session(self, obj, request):
        return StripeService.create_item_session(obj, request)


class PaymentDetailView(DetailView):
    model = Item
    template_name = 'payments/payment_detail.html'
    pk_url_kwarg = 'item_id'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'payments/order_detail.html'
    pk_url_kwarg = 'order_id'


def success(request):
    return render(request, "payments/success.html")


def cancel(request):
    return render(request, "payments/cancel.html")
