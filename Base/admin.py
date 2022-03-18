from django.contrib import admin
from .models import *
# Register your models here.


# class PostImageAdmin(admin.StackedInline):
#     model = PostImage

# @admin.register(productDetail)
# class product(admin.ModelAdmin):
#     list_display = ['id','productName'] 
#     readonly_fields=('QRcodePicture','code')

# @admin.register(productDetail)
# class PostAdmin(admin.ModelAdmin):
#     inlines = [PostImageAdmin]

#     class Meta:
#        model = 




class productImageAdmin(admin.StackedInline):
    model = productImage

@admin.register(productDetail)
class productDetailAdmin(admin.ModelAdmin):
    readonly_fields=('QRcodePicture','code')
    
    inlines = [productImageAdmin]
    class Meta:
       model = productDetail

