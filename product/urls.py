from django.urls import path
from .views import (
    CategoryView,
    ProductView,
    BrandView,
    ShopView,
    CreateShopProductView,


    updateShopProductView,
    DeleteShopProduct
)


urlpatterns = [
    path('shop/',ShopView.as_view(),name='shopview-url'),
    path('shop/<int:id>/',CategoryView.as_view(),name='categoryview-url'),
    path('product/<int:pk>/',ProductView.as_view(),name='productview-url'),
    path('brand/<int:id>/',BrandView.as_view(),name='brandview-url'),





    path('createproduct/',CreateShopProductView.as_view(),name='createproduct-url'),
    path('product/<int:pk>/delete',DeleteShopProduct.as_view(),name='deleteshopproduct-url'),
    path('product/<int:id>/update',updateShopProductView,name='updateshopproduct-url'),


    

]