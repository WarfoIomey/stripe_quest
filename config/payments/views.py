from django.shortcuts import render
from django.views.generic import (
    DetailView,
)

from .models import Item


class PaymentDetailView(DetailView):
    model = Item
    template_name = 'payments/payment_detail.html'
    pk_url_kwarg = 'item_id'