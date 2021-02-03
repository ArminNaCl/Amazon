from django.urls import path
from .views import (
    index,
)

urlpatterns = [
    path('',index.as_view(),name='homeview-url'),
    

]  #hey i know you you will forget what are you doing later so just copy prouductview to his folder good
