from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(productDetail)
class product(admin.ModelAdmin):
    list_display = ['productName'] 
    readonly_fields=('QRcodePicture','code')






@admin.register(transactionsDetail)
class transactions(admin.ModelAdmin):
    list_display=['productID']
