from django.urls import path
from apps.order.views import add_to_cart_view, cart_view, create_order_view, delete_form_cart_view


urlpatterns = [
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/', add_to_cart_view, name='add-to-cart'),
    path('create/', create_order_view, name='create_order'),
    path('delete/<int:product_id>/', delete_form_cart_view, name='delete_form_cart'),
]
