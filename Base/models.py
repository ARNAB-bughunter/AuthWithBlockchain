from django.db import models
from PIL import Image

class productDetail(models.Model):
    productName = models.TextField()
    productDescription = models.TextField()    
    code = models.TextField()
    QRcodePicture = models.ImageField(upload_to='QRcode',blank=True)
    image = models.ImageField(upload_to = 'product')

    created=models.DateTimeField(auto_now=True)
    def resize(self,im,new_height):
        width,height = im.size
        ratio = height/width
        new_width = int(ratio*new_height)
        resized_image = im.resize((new_width,new_height))
        return resized_image
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img=Image.open(self.image.path)
        img_resized = self.resize(img,250)
        img_resized.save(self.image.path)

         