from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import DetailView,ListView ,UpdateView,CreateView,FormView
from django.db.models import Q
from django.contrib.auth.views import get_user_model
from account.forms import UserUpdateForm,ShopUpdateForm
from account.models import Shop
from product.forms import CreateShopProduct
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed,Http404

User = get_user_model()

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
        context['thisurl']= self.request.GET.get('q','')
        return context

    def get(self,request,*args,**kwargs):
        _to =request.GET.get('price_to')
        _from = request.GET.get('price_from')
        _brand = request.GET.get('brand')
        q = request.GET.get('q')
        self.results = Product.objects.all()
        if q:
            self.results = Product.objects.filter(Q(name__icontains =q)| Q(category__name__icontains=q)| Q(brand__name__icontains = q))
        
        if _brand:
            self.results = self.results.filter(brand__id = _brand)
        
        # self.results = self.results.filter(best_price__price__gt =_from)
        self.results = list(set(self.results))
        return super().get(request)

    def get_queryset(self):
        return self.results
              
def myAccountView(request):
    return render(request, 'siteview/my-account.html',{'user':request.user})

@login_required
def updateProfile(request):
    if request.method == 'POST':
        form = UserUpdateForm(data=request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('shopview-url')
    else:
        form=UserUpdateForm(instance=request.user)
    return render(request,'siteview/update_form.html',{'form':form})

@login_required
def updateShop(request,id):
    instance = get_object_or_404(Shop, id=id)
    if instance.user == request.user:
        if request.method == 'POST':
            form = ShopUpdateForm(data=request.POST,instance=instance)
            if form.is_valid():
                form.save()
                return redirect('shopview-url')
        else:
            form=ShopUpdateForm(instance=instance)
        return render(request,'siteview/update_shop_form.html',{'form':form, 'id':id}) 
    else:
        return  HttpResponseNotAllowed('hello')


class CreateShopProductView(CreateView):
    form_class = ShopProduct
    success_url= 'myaccountview-url'
    template_name = 'siteview/checkout.html'
    form_class =CreateShopProduct
        
        # form.shop = self.request.user.shop.all()
    


class CreateShopView(CreateView):
    form_class = Shop
    success_url= 'shopview-url'
    template_name= 'siteview/createshop.html'
    form_class= ShopUpdateForm
    def form_valid(self,form):
        shop = form.save(commit=False)
        shop.user = self.request.user
        shop.save()
        return super().form_valid(form)

class UpdateShopProduct(UpdateView):
    model=ShopProduct
    form_class=CreateShopView
    fields=['price','quantity']
    template_name='siteview/update_shopproduct.html'
    success_url = 'shopview-url'
    def get_context_data()
    # def dispatch(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     if obj.shop.user != self.request.user:
    #         raise Http404("You are not allowed to edit this Post")
    #     return super(UpdateShopProduct, self).dispatch(request, *args, **kwargs)


# def add_shop_product(request,*args,**kwargs):




