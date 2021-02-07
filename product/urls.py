from django.urls import path
from .views import (
    CategoryView,
    ProductView,
    BrandView,
    add_to_cart,
    remove_from_cart,
    CartView,
    ShopView
)


urlpatterns = [
    path('shop/',ShopView.as_view(),name='shopview-url'),
    path('shop/<int:id>/',CategoryView.as_view(),name='categoryview-url'),
    path('product/<int:pk>/',ProductView.as_view(),name='productview-url'),
    path('brand/<int:id>/',BrandView.as_view(),name='brandview-url'),
    path('add-to-cart/<int:id>/',add_to_cart,name='addtocart-url'),
    path('remove-from-cart/<int:id>',remove_from_cart,name='removefromcart-url'),
    path('cart/',CartView.as_view(),name='cartview-url')

]