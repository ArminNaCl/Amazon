from django.urls import path
from .views import (
    add_to_cart,
    remove_from_cart,
    CartView
)


urlpatterns = [

    path('product/<int:id>/addtocart',add_to_cart,name='addtocart-url'),
    path('product/<int:id>/removefromcart',remove_from_cart,name='removefromcart-url'),
    path('cart/',CartView.as_view(),name='cartview-url'),

]