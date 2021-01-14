from django.shortcuts import render
from .models import Category

# Create your views here.

def category(request,id):
    return render(request, 'product/category.html',{'category':id})