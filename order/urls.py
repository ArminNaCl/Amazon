from django.urls import path
from .views import (
    add_to_cart,
    remove_from_cart,
    CartView,
    OrdersView,

    cart_to_order
)


urlpatterns = [

    path('product/<int:id>/addtocart',add_to_cart,name='addtocart-url'),
    path('product/<int:id>/removefromcart',remove_from_cart,name='removefromcart-url'),
    path('cart/',CartView.as_view(),name='cartview-url'),
    path('cart/toorder/',cart_to_order,name='carttoorder-url'),
    path('orders/',OrdersView.as_view(),name='orderview-url'),

]