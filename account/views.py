from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseNotAllowed
from django.views.generic.edit import CreateView 
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView as Login , LogoutView as Logout ,get_user_model
from django.contrib.auth import authenticate, login
from order.models import Basket
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm ,UserLoginForm,UserUpdateForm,ShopUpdateForm
from .models import Shop



User = get_user_model()

# Create your views here.
class RegisteritionView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'siteview/registerition.html'
    success_url = '/'
    def form_valid(self,form):
        valid = super(RegisteritionView, self).form_valid(form)
        email, password  = form.cleaned_data.get('email'), form.cleaned_data.get('password1')
        print(email,password)
        new_user = authenticate(email=email, password=password)
        login(self.request, new_user)
        this_user_basket = Basket.objects.get_or_create(user=self.request.user)
        return valid

class LoginView(Login):
    template_name = 'siteview/login.html'
    form_class = UserLoginForm
    success_url='/'

class LogoutView(Logout):
    next_page = '/'


class CreateShopView(CreateView):
    form_class = Shop
    success_url= 'shopview-url'
    template_name= 'siteview/createshop.html'
    form_class= ShopUpdateForm
    def form_valid(self,form):
        shop = form.save(commit=False)
        shop.user = self.request.user
        shop.save()
        return super().form_valid(form)









@login_required
def updateProfile(request):
    if request.method == 'POST':
        form = UserUpdateForm(data=request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('shopview-url')
    else:
        form=UserUpdateForm(instance=request.user)
    return render(request,'siteview/update_form.html',{'form':form})

@login_required
def updateShop(request,id):
    instance = get_object_or_404(Shop, id=id)
    if instance.user == request.user:
        if request.method == 'POST':
            form = ShopUpdateForm(data=request.POST,instance=instance)
            if form.is_valid():
                form.save()
                return redirect('shopview-url')
        else:
            form=ShopUpdateForm(instance=instance)
        return render(request,'siteview/update_shop_form.html',{'form':form, 'id':id}) 
    else:
        return  HttpResponseNotAllowed('hello')




class ProfileView(DetailView):
    pass
