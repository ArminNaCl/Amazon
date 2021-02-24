from django.db import models
from django.utils.translation import ugettext_lazy as _
from account.models import Shop ,User
from order.models import Order
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.db.models import Sum
# Create your models here.


# COLOR_CHOICES = (
#     ('green','GREEN'),
#     ('blue', 'BLUE'),
#     ('red','RED'),
#     ('orange','ORANGE'),
#     ('black','BLACK'),
# )

# class ShopProductMeta(models.Model):
#     shop_product = models.ForeignKey('ShopProduct',related_name="metas", verbose_name=_("shop product"),
#                                 on_delete=models.CASCADE)
#     color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')

def get_upload_path(instance, filename):
    model = instance.album.model.__class__._meta
    name = model.verbose_name_plural.replace(' ', '_')
    return f'{name}/images/{filename}'

class ImageAlbum(models.Model):
    name = models.CharField(_("name"), max_length=60, default="yes" )

    @property
    def default(self):
        return self.images.filter(default=True).first()
    class Meta:
        verbose_name = _('ImageAlbum')
    def __str__(self):
        return self.name


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
    parent = models.ForeignKey('self',related_name="children",related_query_name="children",
                        verbose_name=_("parent") ,on_delete=models.SET_NULL, null=True,blank=True)
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
    def __str__(self):
        return self.name

class Product(models.Model):
    brand= models.ForeignKey(Brand, related_name="products", verbose_name=_("brand"),
                                on_delete=models.CASCADE)
    category= models.ForeignKey('Category', related_name="products", verbose_name=_("Category"),
                                on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=60, unique=True )
    details = models.TextField(_("details"), max_length=240, )
    album = models.OneToOneField(ImageAlbum, related_name='model', on_delete=models.CASCADE)
    shop_product = models.ManyToManyField(Shop, through= 'ShopProduct' ,related_name='products')
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
    def __str__(self):
        return self.name

    @property
    def price_range(self):
        low= self.product.order_by('price').first().price
        high= self.product.order_by('price').last().price
        return low,high

    @property 
    def best_price(self) :
        queryset= self.product.order_by('price').first()
        return queryset


class Image(models.Model):
    image = models.ImageField(upload_to=get_upload_path)
    default = models.BooleanField(default=False)
    album = models.ForeignKey(ImageAlbum, related_name='images',related_query_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return self.album.__str__()


    
class ProductMeta(models.Model):
    product =models.ForeignKey(Product,on_delete=models.CASCADE ,related_name='metas' ,related_query_name= 'metas')
    label = models.CharField(_("label"), max_length=60)
    value = models.CharField(_("value"), max_length=60)
    class Meta:
        verbose_name = _('ProductMeta')
        verbose_name_plural = _('ProductsMetas')
    def __str__(self):
        return self.product.__str__()+'-'+str(self.label)


class ShopProduct(models.Model):
    shop= models.ForeignKey(Shop, verbose_name=_("shop"),on_delete=models.CASCADE,related_name='product',related_query_name='product')
    product= models.ForeignKey(Product, verbose_name=_("Product"),related_name='product', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.CharField(_("quantity") , max_length=120)
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)

    @property
    def the_offer(self):
        return self.offers.filter(expire=False).first()

    @property   
    def rate(self):
        score = self.comments.all().aggregate(Sum('rate'))
        score = score['rate__sum']
        count = self.comments.all().count()
        if count != 0:
            return score/count
        else:
            return None

    @property
    def like(self):
        likes = Like.objects.filter(product=self).all()
        return likes.count()

    def order_sale(self):
        order = OrderItem.objects.filter(product=self).all().aggregate(Sum('count'))
        order = order['count__sum']
        return order

    
    def sale(self,value):
        self.quantity = str(int(self.quantity) - int(value))
        self.save(update_fields=["quantity"])



    class Meta:
        verbose_name = _('Shop Product')
        verbose_name_plural = _('Shop Products')
    def __str__(self):
        return self.shop.name+' '+self.product.name


class Like(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"),related_name='like_product'
                            ,on_delete=models.CASCADE)
    product = models.ForeignKey(ShopProduct,verbose_name=_("item"),related_name='like_product',
                                on_delete = models.CASCADE)
    class Meta:
        verbose_name = _('like')
        verbose_name_plural = _('likes')
    def __str__(self):
        return self.product.product.name+' '+self.user.first_name

class Comment(models.Model):
    rate = models.IntegerField(_("Rate"),default=1,validators=[MinValueValidator(1), MaxValueValidator(5)])
    content = models.TextField(_("Content"))
    shop_product = models.ForeignKey(ShopProduct, related_name='comments', related_query_name='comments', verbose_name=_(
        "shop product"), on_delete=models.CASCADE)
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    author = models.ForeignKey(User, verbose_name=_(
        "Author"),related_name='comments', on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(_("confirm"), default=True)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ['-create_at']

    def __str__(self):
        return self.shop_product.__str__()

class TrueofferManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(expire=False)


class Offer(models.Model):
    shop_product = models.ForeignKey(ShopProduct,related_name='offers',related_query_name='offers',
                    on_delete=models.CASCADE,verbose_name=_("shop product"))
    percent = models.IntegerField(_('percent'),validators=[MinValueValidator(1), MaxValueValidator(99)])
    expire = models.BooleanField(_('expire'),default=False)
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    expire_at = models.DateTimeField(_('expire date'))

    objects = models.Manager()
    trueoffer =TrueofferManger()
    class Meta:
        verbose_name = _("Offer")
        verbose_name_plural = _("Offers")
        ordering = ['-create_at']


    def __str__(self):
        return self.shop_product.__str__()

    @property
    def new_price(self):
        return round(self.shop_product.price*(100-self.percent)/100,2)

    @property
    def cut_price(self):
        return self.shop_product.price*self.percent/100

    @property
    def make_expire(self):
        today= date.today()
        if self.expire_at > today:
            self.expire = True



