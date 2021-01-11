from django.db import models
from django.utils.translation import ugettext_lazy as _
from account.models import Shop ,User
# Create your models here.

class Brand(models.Model):
    name = models.CharField(_("name"), max_length=60, unique=True )
    details = models.TextField(_("details"), max_length=120, )
    image = models.ImageField(_("logo"), upload_to='media/brand/logo', blank=True, )
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(_("name"), max_length=60, unique=True )
    details = models.TextField(_("details"), max_length=120, )
    image = models.ImageField(_("image"), upload_to='media/category/img', blank=True, )
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
    def __str__(self):
        return self.name

class Product(models.Model):
    brand= models.OneToOneField(Brand, related_name="products", verbose_name=_("brand"),
                                on_delete=models.CASCADE)
    category= models.ForeignKey(Category, related_name="products", verbose_name=_("Category"),
                                on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=60, unique=True )
    details = models.TextField(_("details"), max_length=120, )
    image = models.ImageField(_("logo"), upload_to='media/brand/logo', blank=True, )
    shop_product = models.ManyToManyField(Shop, through= 'ShopProduct')
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
    def __str__(self):
        return self.name
    @property
    def like_count(self):
        querset = Like.objects.filter(prouduct = self,condition=True)
        return querset.count()

    @property
    def disslike_count(self):
        querset = Like.objects.filter(prouduct = self,condition=False)
        return querset.count()    




class Image(models.Model):
    product = models.ForeignKey(Product,related_name="Image", verbose_name=_("Product"),
                                related_query_name='image-product',on_delete=models.CASCADE)
    image = models.ImageField(_("image"), upload_to='product/img', blank=True, )
    
class ProductMeta(models.Model):
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    label = models.CharField(_("label"), max_length=60)
    value = models.IntegerField(_("value"))
    class Meta:
        verbose_name = _('ProductMeta')
        verbose_name_plural = _('ProductsMetas')

class ShopProduct(models.Model):
    shop= models.ForeignKey(Shop, verbose_name=_("shop"),on_delete=models.CASCADE)
    product= models.ForeignKey(Product, verbose_name=_("Product"),on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.CharField(_("quantity") , max_length=120)
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    class Meta:
        verbose_name = _('Shop Product')
        verbose_name_plural = _('Shop Products')
   

class Like(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"),related_name='like_product'
                            ,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,verbose_name=_("item"),related_name='like_product',
                                on_delete = models.CASCADE)
    condition = models.BooleanField(_("Condition"))  
    class Meta:
        verbose_name = _('like')
        verbose_name_plural = _('likes')