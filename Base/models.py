from django.db import models
from PIL import Image

class productDetail(models.Model):
    productName = models.TextField()
    productDescription = models.TextField()    
    code = models.TextField()
    QRcodePicture = models.ImageField(upload_to='QRcode',blank=True)
    image = models.ImageField(upload_to = 'product')

    created=models.DateTimeField(auto_now=True)
    
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img=Image.open(self.image.path)
        height, width = img.size
        img_resized =img.resize((height,width), Image.ANTIALIAS)
        img_resized.save(self.image.path)

         