from django.db import models
from django.utils.translation import ugettext_lazy as _
from account.models import Shop
# Create your models here.
class Brand(models.Model):
    name = models.CharField(_("name"), max_length=60, unique=True )
    details = models.TextField(_("details"), max_length=120, )
    image = models.ImageField(_("logo"), upload_to='brand/logo', blank=True, )

class Category(models.Model):
    name = models.CharField(_("name"), max_length=60, unique=True )
    details = models.TextField(_("details"), max_length=120, )
    image = models.ImageField(_("image"), upload_to='category/img', blank=True, )


class Product(models.Model):
    brand= models.ForeignKey(Brand, related_name="product", verbose_name=_("brand"),
                                on_delete=models.CASCADE)
    category= models.ForeignKey(Category, related_name="product", verbose_name=_("Category"),
                                on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=60, unique=True )
    details = models.TextField(_("details"), max_length=120, )
    image = models.ImageField(_("logo"), upload_to='brand/logo', blank=True, )


class Image(models.Model):
    product = models.ForeignKey(Product,related_name="Image", verbose_name=_("Product"),
                                related_query_name='image-product',on_delete=models.CASCADE)
    image = models.ImageField(_("image"), upload_to='product/img', blank=True, )
    
class ProductMeta(models.Model):
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    label = models.CharField(_("label"), max_length=60)
    value = models.IntegerField(_("value"))

class ShopProduct(models.Model):
    shop= models.ForeignKey(Shop,related_name="Shop", verbose_name=_("shop"),
                            related_query_name='shop-product',on_delete=models.CASCADE)
    product= models.ForeignKey(Shop,related_name="Product", verbose_name=_("Product"),
                            related_query_name='shop-product',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.CharField(_("quantity") , max_length=120)
    

