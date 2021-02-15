from django.contrib import admin
from .models import Brand , Category , Product ,Like ,ProductMeta,ShopProduct,Image,ImageAlbum,Comment,Offer
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
admin.site.register(ProductMeta )
admin.site.register(ShopProduct )
admin.site.register(Image )
admin.site.register(ImageAlbum)
admin.site.register(Comment)
admin.site.register(Offer)

# admin.site.register(ShopProductMeta)
