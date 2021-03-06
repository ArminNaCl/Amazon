from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from product.models import ShopProduct
from .models import Basket ,BasketItem ,Order,OrderItem
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
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

def remove_from_cart(request,id):
    basket_item = get_object_or_404(BasketItem,id=id)
    basket_item.delete()
    return redirect('cartview-url') 


class CartView(ListView):
    context_object_name = 'basket'
    def get(self,request,*args,**kwargs):
        basket = get_object_or_404(Basket,user=request.user)
        self.results = basket.basket_item.all()
        return super().get(request,*args,**kwargs)
    def get_queryset(self):
        return self.results
    template_name= "siteview/cart.html"

class OrdersView(ListView):
    def get(self,request,*args,**kwargs):
        self.results =self.request.user.orders.all()
        return super().get(request,*args,**kwargs)
    def get_queryset(self):
        return self.results
    template_name='siteview/orders.html'
    context_object_name = 'orders'

    

def cart_to_order(request):
    basket = request.user.baskets
    order = Order.objects.create(user=request.user,discription='')
    for item in basket.basket_item.all():
        _shopproduct = item.product
        _offer = item.product.the_offer
        _count = item.quantity
        _price = item.total_price
        order_item =  OrderItem.objects.create(
            order=order,
            product=_shopproduct,
            price=_price,
            offer=_offer,
            count=_count,
        )
        _shopproduct.sale(_count)
        item.delete()
    return redirect('cartview-url') 
