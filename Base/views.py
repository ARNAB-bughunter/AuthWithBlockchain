from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *
from .apps import blockchain_obj
from passlib.hash import pbkdf2_sha256
from django.conf import settings



def index(request):
    return render(request,'index.html')

def verification(request):
    verification=False
    register=False
    pid=request.POST['pid']
    if request.method=='POST': 
        if( pbkdf2_sha256.verify(request.POST['code'].upper(), productDetail.objects.get(id=pid).code) ):
            verification = True
        else:
            messages.info(request,'Wrong Code')
            return redirect('/item/'+pid+'/')
    product = productDetail.objects.get(id=pid)
    productList=blockchain_obj.aboutProduct(pid)
    return render(request,'item.html',{"product":product,"verification":verification,"productList":productList,"register":register})

def register(request):
    verification=False
    register=False
    pid=request.POST['pid']
    if request.method=='POST': 
        blockchain_obj.registerProduct(pid,request.POST['username'],request.POST['city'],request.POST['country'])
        verification=True
        register=True
    product = productDetail.objects.get(id=pid)
    productList=blockchain_obj.aboutProduct(pid)
    return render(request,'item.html',{"product":product,"verification":verification,"productList":productList,"register":register})
    
def itemDetail(request,id):
    verification=False
    register=False
    product = productDetail.objects.get(id=id)
    productList=blockchain_obj.aboutProduct(id)
    return render(request,'item.html',{"product":product,"verification":verification,"productList":productList,"register":register})



def handler404(request,exception):
    return render(request,'404_error.html')

def handler500(request):
    return render(request,'500_error.html')