from django.shortcuts import render
from django.views.generic import TemplateView
from .models import SlideShow
from product.models import Category,Product,ShopProduct,Offer,Brand


# Create your views here.

class index(TemplateView):
    template_name = 'siteview/index.html'
    def get_context_data(self):
        context = super().get_context_data()
        context['slideshow'] = SlideShow.objects.all()
        context['categories'] = Category.objects.all()
        context['newest'] = Product.objects.order_by('create_at')[:4]
        context['offers'] = Offer.trueoffer.order_by('percent')[:4]
        context['brands'] = Brand.objects.all()[:3]
        return context

