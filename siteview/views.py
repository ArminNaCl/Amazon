from django.shortcuts import render
from django.views.generic import TemplateView,DeleteView
from .models import SlideShow
from product.models import Category,Product,ShopProduct


# Create your views here.

class index(TemplateView):
    template_name = 'siteview/index.html'
    def get_context_data(self):
        context = super().get_context_data()
        context['slideshow'] = SlideShow.objects.all()
        context['categories'] = Category.objects.all()
        context['newest'] = Product.objects.order_by('create_at')[:5]
        # context['newest2']= ShopProduct.objects.filter(product__in= context['newest'])

        context['newest2'] = [ShopProduct.objects.filter(product=product_).order_by('price').first() for product_ in context['newest']]

        
        # context['newest2']= map(context['newest'], key=lambda product_: ShopProduct.objects.filter(product=product_).order_by('price')[:1])
        return context

class ProductView(DeleteView):
    template_name= 'siteview/shop-detail.html'
    model = Product
    context_object_name='object'
    # def get_context_data(self):
    #     context=super().get_context_data()
    #     return context