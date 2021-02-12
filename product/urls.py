from django.urls import path
from .views import (
    CategoryView,
    ProductView,
    BrandView,
    add_to_cart,
    remove_from_cart,
    CartView,
    ShopView,
    myAccountView,
    updateProfile,
    CreateShopProductView,
    updateShop,
    CreateShopView,
    updateShopProductView,
    DeleteShopProduct
)


urlpatterns = [
    path('shop/',ShopView.as_view(),name='shopview-url'),
    path('shop/?q=<str:q>',ShopView.as_view(),name='shopviewq-url' ),
    path('shop/<int:id>/',CategoryView.as_view(),name='categoryview-url'),
    path('product/<int:pk>/',ProductView.as_view(),name='productview-url'),
    path('brand/<int:id>/',BrandView.as_view(),name='brandview-url'),
    path('add-to-cart/<int:id>/',add_to_cart,name='addtocart-url'),
    path('remove-from-cart/<int:id>',remove_from_cart,name='removefromcart-url'),
    path('cart/',CartView.as_view(),name='cartview-url'),
    path('profile/',myAccountView,name='myaccountview-url' ),
    path('updateprofile/', updateProfile,name='updateprofile-url'),
    path('createproduct/',CreateShopProductView.as_view(),name='createproduct-url'),
    path('updateshop/<int:id>',updateShop,name='updateshop-url'),
    path('createshop/',CreateShopView.as_view(),name='createshop-url'),
    path('updateshopproduct/<int:id>',updateShopProductView,name='updateshopproduct-url'),
    path('product/<int:pk>/delete',DeleteShopProduct.as_view(),name='deleteshopproduct-url')
    

]