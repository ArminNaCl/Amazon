from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import DetailView,ListView ,UpdateView,CreateView,FormView,DeleteView
from django.db.models import Q
from django.contrib.auth.views import get_user_model
from account.forms import UserUpdateForm,ShopUpdateForm
from account.models import Shop
from product.forms import CreateShopProduct,UpdateShopProduct ,CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed,Http404
from django.urls import reverse_lazy
from django.views.generic.edit import ModelFormMixin 
from django.utils.decorators import method_decorator

User = get_user_model()

from .models import (
    Category, 
    Product,
    ShopProduct,
    Brand,
    Like

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


class ProductView(DetailView,ModelFormMixin):
    template_name= 'siteview/shop-detail.html'
    model = ShopProduct
    context_object_name='product'
    form_class= CommentForm
    success_url ='#'
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['metas'] = self.get_object().product.metas.all()
        context['user'] = self.request.user
        context['form'] = self.get_form()
        context['comments']=self.get_object().comments.all()
        context['like'] = self.get_object().like

        return context

    def post (self,request,*args,**kwargs):
        if self.request.user.is_authenticated :
            # and self.get_object() in self.request.user.orders.order_item.product.all:
            form = self.get_form()
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.shop_product = self.get_object()
                comment.save()
                return self.form_valid(form)

class BrandView(ListView):
    def get_queryset(self):
        queryset = Product.objects.filter(brand=self.kwargs.get('id'))
        return queryset
    context_object_name = 'product'
    paginate_by=9
    template_name = 'siteview/shop.html'




class ShopView(ListView):
    context_object_name = 'product'
    paginate_by=9
    template_name = 'siteview/shop.html'
    def get_context_data(self):
        context = super().get_context_data()
        context['category'] = Category.objects.filter(parent=None)
        context['brand'] = Brand.objects.all()
        context['thisurl']= self.request.GET.get('q','')
        # context['sort_price_hl']= sorted(self.queryset, key=lambda product: product.price ,reverse=True)
        # context['sort_price_lh']= sorted(self.queryset, key=lambda product: product.price)
        # context['sort_sell']= sorted(self.queryset, key=lambda product: product.order_sale)
        # context['sort_popularity']= sorted(self.queryset, key=lambda product: product.like)
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
              
class CreateShopProductView(CreateView):
    success_url= 'myaccountview-url'
    template_name = 'siteview/checkout.html'
    form_class =CreateShopProduct
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

@login_required
def updateShopProductView(request,id):
    instance = get_object_or_404(ShopProduct,id=id)
    if instance.shop.user == request.user:
        if request.method == 'POST':
            form = UpdateShopProduct(data=request.POST,instance=instance)
            if form.is_valid():
                form.save()
                return redirect('shopview-url')
        else:
            form= UpdateShopProduct(instance=instance)
        return render(request,'siteview/update_shopproduct.html',{'form':form, 'id':id}) 
    else:
        return  HttpResponseNotAllowed('hello')

@login_required
def like_product(request,id):
    user = request.user
    product = ShopProduct.objects.get(id=id)
    Like.objects.get_or_create(product=product,user=user)

    return redirect('shopview-url') 

class DeleteShopProduct(DeleteView):
    model = ShopProduct
    success_url = '/'

@method_decorator(login_required, name='dispatch')
class WishListView(ListView):
    context_object_name = 'products'
    paginate_by =9
    template_name="product/wishlist.html"
    def get_queryset(self):
        self.user = self.request.user
        return self.user.like_product.all()
    def get_context_data(self):
        context= super().get_context_data()
        return context


class DeleteLikeView(DeleteView):
    model=Like
    success_url = 'profile/wishlist'
    template_name='product/shopproduct_confirm_delete.html'
    def get_object(self, queryset=None):
        return Like.objects.get(id=self.kwargs.get("id"))





