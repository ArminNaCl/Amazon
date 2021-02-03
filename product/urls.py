from django.urls import path
from .views import (
    category,
    ProductView,
    BrandView,
)


urlpatterns = [
    path('product/<int:pk>/',ProductView.as_view(),name='productview-url'),
    path('category/<int:id>/',category,name='categoryview-url'),
    path('brand/<int:id>/',BrandView.as_view(),name='brandview-url'),

]