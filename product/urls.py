from django.urls import path
from .views import category


urlpatterns = [
    path('<int:id>/',category,name='category-url'),

]