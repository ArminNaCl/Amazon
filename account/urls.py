
from django.urls import path 
from account.views import (
    LoginView,
    RegisteritionView,
    LogoutView,
    ProfileView,
    CreateShopView,


    updateProfile,
    updateShop

)

urlpatterns=[
    path('login/', LoginView.as_view(),name="login-url"),
    path('register/', RegisteritionView.as_view(),name="Registerition-url"),
    path('logout/', LogoutView.as_view(),name="logout-url"),

    path('profile/',ProfileView.as_view(),name='profile-url'),
    path('profile/update', updateProfile,name='updateprofile-url'),

    path('createshop/',CreateShopView.as_view(),name='createshop-url'),
    path('shop/<int:id>/update',updateShop,name='updateshop-url'),

]