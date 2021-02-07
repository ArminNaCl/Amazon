from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView 
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView as Login , LogoutView as Logout ,get_user_model
from .forms import UserRegistrationForm ,UserLoginForm
from django.contrib.auth import authenticate, login

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
        return valid


class LoginView(Login):
    template_name = 'siteview/login.html'
    form_class = UserLoginForm
    success_url='/'

class LogoutView(Logout):
    next_page = '/'

class ProfileView(DetailView):
    pass
