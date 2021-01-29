from django.urls import path
from .views import (
    index,
    ProductView
)

urlpatterns = [
    path('',index.as_view(),name='homeview-url'),
    path('<int:pk>/',ProductView.as_view(),name='productview-url'),

]