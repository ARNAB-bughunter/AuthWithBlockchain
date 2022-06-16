from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *
from .apps import blockchain_obj
from passlib.hash import pbkdf2_sha256
from django.conf import settings
from .forms import productDetailForm
from django.contrib.auth.models import auth
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def index(request):
    if request.user.is_anonymous:
        return render(request,'index.html')
    else:
        return redirect('dashboard/')

def verification(request):
    verification=False
    register=False
    connected=True
    pid=request.POST['pid']
    product = productDetail.objects.get(id=pid)
    productList=blockchain_obj.aboutProduct(pid)
    
    if request.method=='POST': 
        if( pbkdf2_sha256.verify(request.POST['code'].upper(), productDetail.objects.get(id=pid).code) ):
            verification = True
            return render(request,'item.html',{"product":product,"verification":verification,"productList":productList,"register":register,"connected":connected})

        else:
            messages.error(request,'Wrong Code')
            return render(request,'item.html',{"product":product,"verification":verification,"productList":productList,"register":register,"connected":connected})


    return render(request,'item.html',{"product":product,"verification":verification,"productList":productList,"register":register,"connected":connected})


def sendmail(tx_hash,link,email):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Register Successfully"
    html = """\
    <!DOCTYPE html>
        <html lang="en" >
        <head>
          <meta charset="UTF-8">
          <title>CodePen - Build an HTML Email Template From Scratch</title>
          

        </head>
        <body>
        <!-- partial:index.partial.html -->
        <!DOCTYPE html>
        <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width,initial-scale=1">
          <meta name="x-apple-disable-message-reformatting">
          <title></title>
          <!--[if mso]>
          <noscript>
            <xml>
              <o:OfficeDocumentSettings>
                <o:PixelsPerInch>96</o:PixelsPerInch>
              </o:OfficeDocumentSettings>
            </xml>
          </noscript>
          <![endif]-->
          <style>
            table, td, div, h1, p {font-family: Arial, sans-serif;}
          </style>
        </head>
        <body style="margin:0;padding:0;">
          <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;background:#ffffff;">
            <tr>
              <td align="center" style="padding:0;">
                <table role="presentation" style="width:602px;border-collapse:collapse;border:1px solid #cccccc;border-spacing:0;text-align:left;">
                  <tr>
                    <td align="center" style="padding:40px 0 30px 0;background:#70bbd9;">
                      <p style="padding: 2rem;font-size: 25px;font-weight: bolder;box-shadow:  20px 20px 50px grey">ORIGINX</p>
                      <img src="http://ihub.asu.edu.eg/uploads/1/4/0/8/14081679/blockchain-1_3.jpg" alt="" width="300" style="height:auto;display:block;">
                      
                    </td>
                  </tr>
                  <tr>


                  </tr>
                  <tr>
                    <td style="padding:36px 30px 42px 30px;">
                      <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;">
                        <tr>
                          <td style="padding:0 0 36px 0;color:#153643;">
                            
                            <h1 style="font-size:24px;margin:0 0 20px 0;font-family:Arial,sans-serif;">This is Your Transaction Hash</h1>
                            <p style="word-break: break-all;font-weight: bold;font-size: 15px;">"""+tx_hash+"""</p>
                            <p style="margin:0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;"><a href=" """ +link+""" " style="color:#ee4c50;text-decoration:none;">For More Detail Press Here</a></p>
                            <br><br><br>

                            <h1 style="font-size:24px;margin:0 0 20px 0;font-family:Arial,sans-serif;">Thank You For Useing ORIGINX</h1>
                            <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tempus adipiscing felis, sit amet blandit ipsum volutpat sed. Morbi porttitor, eget accumsan et dictum, nisi libero ultricies ipsum, posuere neque at erat.</p>
                            
                          </td>
                        </tr>
                        
                  <tr>
                    <td style="padding:30px;background:#ee4c50;">
                      <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;font-size:9px;font-family:Arial,sans-serif;">
                        <tr>
                          <td style="padding:0;width:50%;" align="left">
                            <p style="margin:0;font-size:14px;line-height:16px;font-family:Arial,sans-serif;color:#ffffff;">
                              &reg; Someone, Somewhere 2022<br/>
                            </p>
                          </td>
                          <td style="padding:0;width:50%;" align="right">
                            <table role="presentation" style="border-collapse:collapse;border:0;border-spacing:0;">
                              <tr>
                                <td style="padding:0 0 0 10px;width:38px;">
                                  <a href="http://www.twitter.com/" style="color:#ffffff;"><img src="https://assets.codepen.io/210284/tw_1.png" alt="Twitter" width="38" style="height:auto;display:block;border:0;" /></a>
                                </td>
                                <td style="padding:0 0 0 10px;width:38px;">
                                  <a href="http://www.facebook.com/" style="color:#ffffff;"><img src="https://assets.codepen.io/210284/fb_1.png" alt="Facebook" width="38" style="height:auto;display:block;border:0;" /></a>
                                </td>
                              </tr>
                            </table>
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
        </body>
        </html>
        <!-- partial -->
          
        </body>
        </html>
    """
    part = MIMEText(html, "html")
    message.attach(part)
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login('testnaha420@gmail.com', 'jzckhqjzjzhzhvob')
    s.sendmail('testnaha420@gmail.com', email, message.as_string())
    s.quit()

def register(request):
    verification=False
    register=False
    connected=True
    pid=request.POST['pid']
    link = productDetail.objects.get(id=int(pid)).link
    manufacturer=productDetail.objects.get(id=int(pid)).manufacturer
    productName=productDetail.objects.get(id=int(pid)).productName

    if request.method=='POST': 
        tx_hash=blockchain_obj.registerProduct(pid,request.POST['username'],request.POST['ownership'],request.POST['city'],request.POST['country'])
        transactionsDetail(productID=pid,manufacturer=manufacturer,tx_hash=tx_hash).save()
        sendmail(tx_hash,link,request.POST['useremail'])
        if request.POST['ownership']=='Distributer':
            sellRecord(productID=pid,productName=productName,manufacturer=manufacturer,link=link,sellType=1).save()
        elif request.POST['ownership']=='Retailer':
            sellRecord(productID=pid,productName=productName,manufacturer=manufacturer,link=link,sellType=2).save()
        else:
            sellRecord(productID=pid,productName=productName,manufacturer=manufacturer,link=link,sellType=3).save()
        
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
        messages.success(request, 'Metamask Account Connected')
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
            blockchain_obj.setDefaultAccount()
            return redirect('dashboard/')
        else:
            messages.error(request,"Invalid Credential")
            return render(request,'auth.html')

def signup(request):
    if request.method=='POST':
        if User.objects.filter(companyName=request.POST['company']).exists():
            messages.error(request,"Company Name Already Taken")
        elif User.objects.filter(phone=request.POST['phone']).exists():
            messages.error(request,"Phone Number Already Taken")
        elif  User.objects.filter(email=request.POST['email']).exists():
            messages.error(request,"Email Already Taken")
        elif User.objects.filter(username=request.POST['username']).exists():
            messages.error(request,"Username Already Taken")
        else:
            User.objects.create_user(companyName=request.POST['company'],phone=request.POST['phone'],email=request.POST['email'],username=request.POST['username'],password=request.POST['password'])
            messages.success(request,"Account  Created")
        return redirect('/auth/')

def dashboard(request):
    allproduct = productDetail.objects.filter(manufacturer=request.user.companyName)
    sellproduct = sellRecord.objects.filter(manufacturer=request.user.companyName)
    allproductCount = productDetail.objects.filter(manufacturer=request.user.companyName).count()
    totalSellCount = sellRecord.objects.filter(manufacturer=request.user.companyName).values('productID').distinct().count()
    distributerCount = sellRecord.objects.filter(manufacturer=request.user.companyName,sellType=1).count()
    retailerCount = sellRecord.objects.filter(manufacturer=request.user.companyName,sellType=2).count()
    endCustomerCount = sellRecord.objects.filter(manufacturer=request.user.companyName,sellType=3).count()
    return render(request,'dashboard.html',{'allproduct':allproduct,'sellproduct':sellproduct,'sell':totalSellCount,'register':allproductCount,'distributerCount':distributerCount,'retailerCount':retailerCount,'endCustomerCount':endCustomerCount})

def blockchain(request):
    return render(request,'blockchain.html')

def signout(request):
    auth.logout(request)
    return redirect('/')

def handler404(request,exception):
    return render(request,'404_error.html')

def handler500(request):
    return render(request,'500_error.html')