from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Basket(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"),related_name='baskets'
                                ,on_delete=models.CASCADE)
    
    @property
    def total_price(self):
        total = 0
        all_items = self.basket_item.all()
        for items in all_items:
            total += items.total_price
        return total

    @property
    def sub_total(self):
        total =0
        all_items = self.basket_item.all()
        for item in all_items:
            total += item.product.price
        return total


    @property
    def final_cut(self):
        return self.sub_total - self.total_price




    class Meta:
        verbose_name = _('basket')
        verbose_name_plural = _('baskets')
    def __str__(self):
        return str(self.user.last_name)


class BasketItem(models.Model):
    basket = models.ForeignKey('order.Basket',verbose_name=_("basket"),related_name='basket_item',
                                on_delete= models.CASCADE)
    product = models.ForeignKey('product.ShopProduct',verbose_name=_("item"),related_name='basket_item',
                                on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    @property
    def total_price(self):
        print("f")
        if self.product.the_offer:
            print('hey')
            return self.product.the_offer.new_price*self.quantity
        else:
            return self.product.price*self.quantity

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
    def __str__(self):
        return str(self.user.last_name)+' order '+str(self.create_at)
    

class OrderItem(models.Model):
    order= models.ForeignKey(Order,verbose_name=_('order'), related_name= 'order_item',
                            on_delete=models.CASCADE)
    product = models.ForeignKey('product.ShopProduct',verbose_name=_("item"),related_name='order_item',
                                on_delete = models.PROTECT)
    offer = models.ForeignKey('product.Offer',verbose_name=_('offer') , on_delete = models.PROTECT ,null=True)
    count = models.IntegerField(_('count'))
    price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name = _('order_item')
        verbose_name_plural = _('order_items')



class Payment(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"),related_name='payment'
                            ,on_delete=models.CASCADE)
    order = models.OneToOneField(Order, verbose_name=_("order"),related_name='payment'
                                ,on_delete=models.CASCADE)
    amount = models.IntegerField(_('amount'))
    class Meta:
        verbose_name = _('payment')
        verbose_name_plural = _('payments')
    

