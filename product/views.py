from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import DeleteView,ListView
from .models import (
    Category, 
    Product,
    ShopProduct,

)

from order.models import (
    Basket,
    BasketItem
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

def add_to_cart(request,id):
    product = get_object_or_404(ShopProduct,id=id)
    basket = Basket.objects.get(user=request.user)
    if basket.basket_item.filter(product=product):
        basket_item = basket.basket_item.get(product=product)
        basket_item.quantity +=1
        basket_item.save()

    else:
        basket_item = BasketItem.objects.create(product=product,basket=basket)

    return  redirect("productview-url",product.id)




class CartView(ListView):
    context_object_name = 'basket'
    def get(self,request,*args,**kwargs):
        basket = Basket.objects.get(user=request.user)
        self.results = basket.basket_item.all()
        return super().get(request,*args,**kwargs)

    def get_queryset(self):
        return self.results


    template_name= "siteview/cart.html"