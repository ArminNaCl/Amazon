from django.contrib import admin
from .models import User, Shop , Address 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as  _ 

from django.contrib.auth.forms import AdminPasswordChangeForm

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['email' , 'mobile', 'last_name']
    change_password_form = AdminPasswordChangeForm
    ordering =('last_name','email')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1','password2','mobile')
        }),
    )
    fieldsets = (
        (_('authentication data'), {
            "fields": (
                'email',
                'password',
            ),
        }),
        (_('Personal info'), {
            "fields": ('mobile','first_name','last_name', 'image')
        }),
        (_('Permissions'), {
            "fields": ('is_staff', 'is_active', 'is_superuser',)
        }),
        (_('Important dates'), {
            "fields": ('last_login',)
        }),
    )



# class ShopAdmin(admin.TabularInline):
#     model = Shop

admin.site.register(Shop)
admin.site.register(Address)
