from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Basket(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"),related_name='baskets'
                                ,on_delete=models.CASCADE)
    class Meta:
        verbose_name = _('basket')
        verbose_name_plural = _('baskets')


from product.models import ShopProduct ,Product
class BasketItem(models.Model):
    basket = models.ForeignKey(Basket,verbose_name=_("basket"),related_name='basket_item',
                                on_delete= models.CASCADE)
    product = models.ForeignKey(ShopProduct,verbose_name=_("item"),related_name='basket_item',
                                on_delete = models.CASCADE)
    class Meta:
        verbose_name = _('basket_item')
        verbose_name_plural = _('basket_items')
    

class Order(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"),related_name='orders'
                            ,on_delete=models.CASCADE)
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    discription = models.TextField(_('discription'), max_length=120)
    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')
    

class OrderItem(models.Model):
    order= models.ForeignKey(Order,verbose_name=_('order'), related_name= 'order_item',
                            on_delete=models.CASCADE)
    product = models.ForeignKey(ShopProduct,verbose_name=_("item"),related_name='order_item',
                                on_delete = models.CASCADE)
    count = models.IntegerField(_('count'))
    price = models.IntegerField(_('price'))

    class Meta:
        verbose_name = _('order_item')
        verbose_name_plural = _('order_items')

    @property
    def total_price(self):
        return self.price*self.count

class Payment(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"),related_name='payment'
                            ,on_delete=models.CASCADE)
    order = models.OneToOneField(Order, verbose_name=_("order"),related_name='payment'
                                ,on_delete=models.CASCADE)
    amount = models.IntegerField(_('amount'))
    class Meta:
        verbose_name = _('payment')
        verbose_name_plural = _('payments')
    

