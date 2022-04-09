from django.db import models
from PIL import Image
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    companyName=models.TextField()
    phone=models.TextField()

class productDetail(models.Model):
    productName = models.TextField()
    productDescription = models.TextField()    
    code = models.TextField()
    QRcodePicture = models.ImageField(upload_to='QRcode',blank=True)
    image = models.ImageField(upload_to = 'product')
    manufacturer = models.TextField()
    created=models.DateTimeField(auto_now=True)
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img=Image.open(self.image.path)
        height, width = img.size
        img_resized =img.resize((height,width), Image.ANTIALIAS)
        img_resized.save(self.image.path)


class transactionsDetail(models.Model):
    productID = models.CharField(max_length=100,null=False,blank=False)
    tx_hash = models.TextField()
    created = models.DateTimeField(auto_now=True)


