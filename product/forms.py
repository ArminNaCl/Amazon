from django import forms
from .models import ShopProduct



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