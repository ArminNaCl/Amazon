from django import forms
from .models import ShopProduct ,Comment
from django.utils.translation import ugettext_lazy as _



class CreateShopProduct(forms.ModelForm):
    class Meta:
        model = ShopProduct
        fields = ['shop','product','price','quantity']
        widgets={
            'shop'      :   forms.Select(attrs={'class':"form-control"}),
            'product'   :   forms.Select(attrs={'class':"form-control"}),
            'price'     :   forms.TextInput(attrs={'class':"form-control"}),
            'quantity'  :   forms.TextInput(attrs={'class':"form-control"}),
        }
    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user')
        super().__init__(*args,**kwargs)
        self.fields['shop'].queryset = user.shop.all()

class UpdateShopProduct(forms.ModelForm):
    class Meta:
        model = ShopProduct
        fields = ['price','quantity']
        widgets={
            'price'     :   forms.TextInput(attrs={'class':"form-control"}),
            'quantity'  :   forms.TextInput(attrs={'class':"form-control"}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'content', 'rate'}
        labels = {'content':_('Comment'),'rate':_('Rate')}
        help_text = {
                    'content' :_("enter your comment about this post"),
        }
        widgets={
            'content': forms.Textarea(attrs={'class':"form-control"}),
            'rate': forms.NumberInput(attrs={'class':"form-control"}),
        }