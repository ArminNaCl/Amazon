from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseNotAllowed
from django.views.generic.edit import CreateView ,DeleteView,UpdateView
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView as Login , LogoutView as Logout ,get_user_model
from django.contrib.auth import authenticate, login
from order.models import Basket
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm ,UserLoginForm,UserUpdateForm,ShopUpdateForm,AddressCreateForm
from .models import Shop,Address



User = get_user_model()

# Create your views here.
class RegisteritionView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'account/registerition.html'
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
    template_name = 'account/login.html'
    form_class = UserLoginForm
    success_url='profile/update/'

class LogoutView(Logout):
    next_page = '/'


class CreateShopView(CreateView):
    form_class = Shop
    success_url= 'shopview-url'
    template_name= 'account/create_shop.html'
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
    return render(request,'account/update_profile.html',
            context={'form':form,'user':request.user,
                    'shops':Shop.objects.filter(user=request.user)})

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
        return render(request,'account/update_shop.html',{'form':form, 'id':id}) 
    else:
        return  HttpResponseNotAllowed('hello')

class DeleteShopView(DeleteView):
    model=Shop
    success_url = 'profile/update'
    template_name='product/shopproduct_confirm_delete.html'
    def get_object(self, queryset=None):
        return Shop.objects.get(id=self.kwargs.get("id"))



class EditAddressView(UpdateView):
    model = Address
    fields=['city','street','allay','zip_code']
    success_url = 'profile/update'
    template_name = 'account/update_address.html'
    def get_object(self, queryset=None):
        return Address.objects.get(id=self.kwargs.get("id"))

class CreateAddressView(CreateView):
    model = Address
    fields=['city','street','allay','zip_code']
    form = AddressCreateForm
    success_url = 'profile/update'
    template_name = 'account/add_address.html'
    def form_valid(self,form):
        add = form.save(commit=False)
        add.user =self.request.user
        add.save()
        return super().form_valid(form)

class DeleteAddressView(DeleteView):
    model=Address
    success_url = 'profile/update'
    template_name='product/shopproduct_confirm_delete.html'
    def get_object(self, queryset=None):
        return Address.objects.get(id=self.kwargs.get("id"))



        


class ProfileView(DetailView):
    pass
