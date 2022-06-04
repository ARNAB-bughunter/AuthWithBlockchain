from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *
from .apps import blockchain_obj
from passlib.hash import pbkdf2_sha256
from django.conf import settings
from .forms import productDetailForm
from django.contrib.auth.models import auth

def index(request):
    if request.user.is_anonymous:
        return render(request,'index.html')
    else:
        return render(request,'index.html')

def verification(request):
    verification=False
    register=False
    connected=True
    pid=request.POST['pid']
    if request.method=='POST': 
        if( pbkdf2_sha256.verify(request.POST['code'].upper(), productDetail.objects.get(id=pid).code) ):
            verification = True
        else:
            messages.info(request,'Wrong Code')
            return redirect('/item/'+pid+'/')
    product = productDetail.objects.get(id=pid)
    productList=blockchain_obj.aboutProduct(pid)
    return render(request,'item.html',{"product":product,"verification":verification,"productList":productList,"register":register,"connected":connected})

def register(request):
    verification=False
    register=False
    connected=True
    pid=request.POST['pid']
    manufacturer=productDetail.objects.get(id=int(pid)).manufacturer
    if request.method=='POST': 
        tx_hash=blockchain_obj.registerProduct(pid,request.POST['username'],request.POST['ownership'],request.POST['city'],request.POST['country'])
        transactionsDetail(productID=pid,manufacturer=manufacturer,tx_hash=tx_hash).save()
        verification=True
        register=True
    product = productDetail.objects.get(id=pid)
    productList=blockchain_obj.aboutProduct(pid)
    return render(request,'item.html',{"product":product,"verification":verification,"productList":productList,"register":register,"connected":connected})

def setUser(request):
    verification=False
    register=False
    connected=False
    pid=request.POST['pid']
    if request.method=='POST':
        useraddres = request.POST['useraddress']
        blockchain_obj.setAccount(useraddres)
        connected = True
        print(useraddres)


    product = productDetail.objects.get(id=pid)
    productList=blockchain_obj.aboutProduct(pid)
    return render(request,'item.html',{"product":product,"verification":verification,"productList":productList,"register":register,"connected":connected})



def itemDetail(request,id):
    verification=False
    register=False
    connected=False
    product = productDetail.objects.get(id=id)
    productList=blockchain_obj.aboutProduct(id)
    return render(request,'item.html',{"product":product,"verification":verification,"productList":productList,"register":register,"connected":connected})

def qrcreate(request):
    form=productDetailForm()
    product=None
    if request.method=='POST':
        fm=productDetailForm(request.POST,request.FILES)
        if fm.is_valid():
            productName=fm.cleaned_data['productName']
            productDescription=fm.cleaned_data['productDescription']
            image=fm.cleaned_data['image']
            productdetail=productDetail(productName=productName,productDescription=productDescription,manufacturer=request.user.companyName,image=image)
            productdetail.save()     
            product = productdetail      
            blockchain_obj.registerProduct(str(productdetail.pk),productdetail.manufacturer,'Manufacturer','--','--')
            return render(request,'qrgenarate.html',{'form':fm,'product':product})

    return render(request,'qrgenarate.html',{'form':form,'product':product})

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def authentication(request):
    return render(request,'auth.html')

def signin(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            print(request.user.companyName)
            return redirect('dashboard/')
        else:
            messages.error(request,"Invalid Credential")
            return render(request,'auth.html')

def signup(request):
    if request.method=='POST':
        User.objects.create_user(companyName=request.POST['company'],phone=request.POST['phone'],email=request.POST['email'],username=request.POST['username'],password=request.POST['password'])
        return redirect('/auth/')

def dashboard(request):
    allproduct=productDetail.objects.filter(manufacturer=request.user.companyName)
    return render(request,'dashboard.html',{'allproduct':allproduct})

def blockchain(request):
    return render(request,'blockchain.html')

def signout(request):
    auth.logout(request)
    return redirect('/')

def handler404(request,exception):
    return render(request,'404_error.html')

def handler500(request):
    return render(request,'500_error.html')