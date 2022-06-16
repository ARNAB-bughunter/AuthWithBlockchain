from random import randint
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from .models import *
from django.conf import settings
import qrcode
import cv2
from passlib.hash import pbkdf2_sha256
from .apps import blockchain_obj

@receiver(pre_save,sender=productDetail)
def CodeIdGenarate(sender,instance,**kwargs):
    id = ''.join(["{}".format(randint(0,9)) for num in range(0,7)])
    code = ''.join(["{}".format(chr(randint(65, 90))) for num in range(0,7)])
    temp_code = code
    code = pbkdf2_sha256.using(rounds=8000, salt_size=10).hash(code)
    x =  settings.APP_URL+"item/"+str(id)+"/"
    img = qrcode.make(x)
    instance.code = code
    instance.id = id
    instance.link = x
    y = str(instance.id)+'.png'
    z = 'QRcode/'+y
    img.save(settings.BASE_DIR/'media'/'QRcode'/y)    
    instance.QRcodePicture = z
    temp=settings.BASE_DIR/'media'/'QRcode'/y
    temp=temp.as_posix()
    image = cv2.imread(temp)
    image = cv2.putText(image, temp_code, (135,365), cv2.FONT_HERSHEY_COMPLEX_SMALL,1, (0,0,0),2)
    cv2.imwrite(temp, image)