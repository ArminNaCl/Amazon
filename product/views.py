from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import DetailView,ListView
from .models import (
    Category, 
    Product,
    ShopProduct,
    Brand,

)

from order.models import (
    Basket,
    BasketItem
)
# Create your views here.

class CategoryView(ListView):
    def get_queryset(self):
        queryset = Product.objects.filter(category=self.kwargs.get('id'))
        return queryset
    context_object_name = 'product'
    paginate_by=9
    template_name = 'siteview/shop.html'
    def get_context_data(self):
        context = super().get_context_data()
        context['category'] = Category.objects.filter(parent=None)
        context['brand'] = Brand.objects.all()
        context['select'] = Category.objects.get(id =self.kwargs.get('id'))
        return context


def category(request,id):
    return render(request, 'product/category.html',{'category':id})


class ProductView(DetailView):
    template_name= 'siteview/shop-detail.html'
    model = Product
    context_object_name='product'
    # def get_context_data(self):
    #     context=super().get_context_data()
    #     context['image'] = 
    #     return context

class BrandView(DetailView):
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

def remove_from_cart(request,id):
    basket_item = get_object_or_404(BasketItem,id=id)
    basket_item.delete()
    return redirect('cartview-url') 




class CartView(ListView):
    context_object_name = 'basket'
    def get(self,request,*args,**kwargs):
        basket = Basket.objects.get(user=request.user)
        self.results = basket.basket_item.all()
        return super().get(request,*args,**kwargs)

    def get_queryset(self):
        return self.results


    template_name= "siteview/cart.html"

class ShopView(ListView):
    context_object_name = 'product'
    paginate_by=9
    template_name = 'siteview/shop.html'
    def get_context_data(self):
        context = super().get_context_data()
        context['category'] = Category.objects.filter(parent=None)
        context['brand'] = Brand.objects.all()
        return context
    def get(self,request):
        _to =request.GET.get('price_to')
        _from = request.GET.get('price_from')
        q = request.GET.get('q','')
        result=list()
        result += Product.objects.filter(name__icontains = q)
        result += Product.objects.filter(category__name__icontains = q)
        result += Product.objects.filter(brand__name__icontains = q)
        self.results = list(set(result))
        self.results.objects.filter
        return super().get(request)
    def get_queryset(self):
        if self.results:
            return self.results
        else:
            return Product.objects.all()
        


