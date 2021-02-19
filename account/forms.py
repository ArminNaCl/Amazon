from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import password_validation ,  get_user_model 
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm ,UsernameField
from .models import Shop ,Address

User = get_user_model()


        


class UserRegistrationForm (UserCreationForm ) :
    email= forms.EmailField(max_length=120 ,widget=forms.EmailInput(attrs={'class':"form-control"}))
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':"form-control"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password' ,'class':"form-control"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    class Meta:
        model = User
        fields ={'email','first_name','last_name','mobile','password1','password2'}
        widgets={
            'first_name' : forms.TextInput(attrs={'class':"form-control"}),
            'last_name' : forms.TextInput(attrs={'class':"form-control"}),
            'mobile' :  forms.TextInput(attrs={'class':"form-control"}),
            
        }

class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,'class':"form-control"}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':"form-control"}),
    )

class UserUpdateForm(forms.ModelForm):

    
    class Meta:
        model=User
        fields=['image','first_name','last_name','email','mobile']
        widgets={
            'first_name' : forms.TextInput(attrs={'class':"form-control"}),
            'last_name' : forms.TextInput(attrs={'class':"form-control"}),
            'mobile' :  forms.TextInput(attrs={'class':"form-control"}),
            'email' : forms.TextInput(attrs={'class':"form-control"}),   
        }
    def save(self,commit=True):
        user =self.instance
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.mobile = self.cleaned_data['mobile']
        user.email = self.cleaned_data['email']
        if self.cleaned_data['image']:
            print("im in")
            user.image= self.cleaned_data['image']
        if commit:
            user.save()
        return user





class ShopUpdateForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields=['name','discription','image']
        widgets={
            'name' : forms.TextInput(attrs={'class':"form-control"}),
            'discription' : forms.Textarea(attrs={'class':"form-control"}),
        }

class AddressCreateForm(forms.ModelForm):
    class Meta:
        model=Address 
        fields = ['city','street','allay','zip_code']
        widgets={
            'city' : forms.TextInput(attrs={'class':"form-control"}),
            'street' : forms.TextInput(attrs={'class':"form-control"}),
            'allay' :  forms.TextInput(attrs={'class':"form-control"}),
            'zip_code' : forms.NumberInput(attrs={'class':"form-control"}),  
        }
