from django.urls import path
from .views import (
    CategoryView,
    ProductView,
    BrandView,
    ShopView,
    CreateShopProductView,
    WishListView,
    DeleteLikeView,
    AddOfferView,


    updateShopProductView,
    DeleteShopProduct,
    like_product
)


urlpatterns = [
    path('shop/',ShopView.as_view(),name='shopview-url'),
    path('shop/<int:id>/',CategoryView.as_view(),name='categoryview-url'),
    path('product/<int:pk>/',ProductView.as_view(),name='productview-url'),
    path('brand/<int:id>/',BrandView.as_view(),name='brandview-url'),

    path('product/<int:id>/offer/',AddOfferView.as_view(),name='addoffer-url'),


    path('createproduct/',CreateShopProductView.as_view(),name='createproduct-url'),
    path('product/<int:pk>/delete',DeleteShopProduct.as_view(),name='deleteshopproduct-url'),
    path('product/<int:id>/update',updateShopProductView,name='updateshopproduct-url'), 
    path('product/<int:id>/like',like_product,name='likeshopproduct-url'),
    
    path('profile/wishlist/<int:id>/remove',DeleteLikeView.as_view(),name='removelike-url'),

    path('profile/wishlist/' ,WishListView.as_view(),name='wishlistview-url'),

    


    

]