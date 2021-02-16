
from django.urls import path 
from account.views import (
    LoginView,
    RegisteritionView,
    LogoutView,
    ProfileView,
    CreateShopView,
    EditAddressView,
    CreateAddressView,
    DeleteAddressView,
    DeleteShopView,

    updateProfile,
    updateShop,


    
    

)

urlpatterns=[
    path('login/', LoginView.as_view(),name="login-url"),
    path('register/', RegisteritionView.as_view(),name="Registerition-url"),
    path('logout/', LogoutView.as_view(),name="logout-url"),

    path('profile/',ProfileView.as_view(),name='updateprofile-url'),
    path('profile/update', updateProfile,name='profile-url'),

    path('shop/add',CreateShopView.as_view(),name='createshop-url'),
    path('shop/<int:id>/update',updateShop,name='updateshop-url'),
    path('shop/<int:id>/delete',DeleteShopView.as_view(),name='deleteshop-url'),

    path('profile/address/add',CreateAddressView.as_view(),name='addaddress-url'),
    path('profile/address/<int:id>/update',EditAddressView.as_view(),name='editaddress-url'),
    path('profile/address/<int:id>/delete',DeleteAddressView.as_view(),name='deleteaddress-url'),


]