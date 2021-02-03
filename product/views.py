from django.shortcuts import render
from django.views.generic import DeleteView
from .models import (
    Category, 
    Product,

)
# Create your views here.

def category(request,id):
    return render(request, 'product/category.html',{'category':id})


class ProductView(DeleteView):
    template_name= 'siteview/shop-detail.html'
    model = Product
    context_object_name='product'
    # def get_context_data(self):
    #     context=super().get_context_data()
    #     context['image'] = 
    #     return context

class BrandView(DeleteView):
    pass