from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(User)
class user(admin.ModelAdmin):
    list_display = ['username','first_name','last_name'] 

@admin.register(productDetail)
class product(admin.ModelAdmin):
    list_display = ['productName'] 
    readonly_fields=('QRcodePicture','code')

@admin.register(sellRecord)
class sell(admin.ModelAdmin):
    list_display=['productID']

@admin.register(transactionsDetail)
class transactions(admin.ModelAdmin):
    list_display=['productID']
