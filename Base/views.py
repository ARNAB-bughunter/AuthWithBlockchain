from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *
from .apps import blockchain_obj
from passlib.hash import pbkdf2_sha256
from django.conf import settings
from .forms import productDetailForm


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
        tx_hash=blockchain_obj.registerProduct(pid,request.POST['username'],request.POST['ownership'],request.POST['city'],request.POST['country'])
        transactionsDetail(productID=pid,tx_hash=tx_hash).save()
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

def qrcreate(request):
    form=productDetailForm()
    product=None
    if request.method=='POST':
        fm=productDetailForm(request.POST,request.FILES)
        if fm.is_valid():
            productName=fm.cleaned_data['productName']
            productDescription=fm.cleaned_data['productDescription']
            manufacturer=fm.cleaned_data['manufacturer']
            image=fm.cleaned_data['image']
            productdetail=productDetail(productName=productName,productDescription=productDescription,manufacturer=manufacturer,image=image)
            productdetail.save()     
            product = productdetail      
            blockchain_obj.registerProduct(str(productdetail.pk),productdetail.manufacturer,'Manufacturer','--','--')
            return render(request,'qrgenarate.html',{'form':fm,'product':product})

    return render(request,'qrgenarate.html',{'form':form,'product':product})

def handler404(request,exception):
    return render(request,'404_error.html')

def handler500(request):
    return render(request,'500_error.html')