from django.urls import path
from .views import (
    category,
    ProductView,
    BrandView,
    add_to_cart,
    remove_from_cart,
    CartView
)


urlpatterns = [
    path('product/<int:pk>/',ProductView.as_view(),name='productview-url'),
    path('category/<int:id>/',category,name='categoryview-url'),
    path('brand/<int:id>/',BrandView.as_view(),name='brandview-url'),
    path('add-to-cart/<int:id>/',add_to_cart,name='addtocart-url'),
    path('remove-from-cart/<int:id>',remove_from_cart,name='removefromcart-url'),
    path('cart/',CartView.as_view(),name='cartview-url')

]