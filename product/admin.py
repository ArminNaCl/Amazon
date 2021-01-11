from django.contrib import admin
from .models import Brand , Category , Product ,Like
# Register your models here.


# class BrandAdmin(admin.TabularInline):
#     model = Brand



# class CategoryAdmin(admin.TabularInline):
#     model = Category


# class ProductAdmin(admin.TabularInline):
#     model = Product

admin.site.register(Brand )
admin.site.register(Category )
admin.site.register(Product )
admin.site.register(Like )