from django.urls import path

from . import views


app_name = 'payments'

urlpatterns = [
    path(
        'item/<int:item_id>/',
        views.PaymentDetailView.as_view(),
        name='detail_payment'
    ),
    path(
        'order/<int:order_id>/',
        views.OrderDetailView.as_view(),
        name='detail_order'
    ),
    path(
        'buy/<int:item_id>/',
        views.BuyItemView.as_view(),
        name='create_checkout_session'
    ),
    path(
        'buy-order/<int:order_id>/',
        views.BuyOrderView.as_view(),
        name='buy_order'
    ),
    path("success/", views.success, name="success"),
    path("cancel/", views.cancel, name="cancel"),
]