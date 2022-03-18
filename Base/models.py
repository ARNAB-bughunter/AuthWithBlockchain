from django.db import models
from PIL import Image

class productDetail(models.Model):
    productName = models.TextField()
    productDescription = models.TextField()    
    code = models.TextField()
    QRcodePicture = models.ImageField(upload_to='QRcode',blank=True)
    created=models.DateTimeField(auto_now=True)

class productImage(models.Model):
    productdetail = models.ForeignKey(productDetail, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'product')
    