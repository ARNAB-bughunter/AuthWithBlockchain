from django.apps import AppConfig
import sys
from Base.connection import myBlockchain
from os import system
from django.conf import settings

blockchain_obj=None

class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Base'

    def ready(self,*args,**kwargs):
        import Base.signals
        global blockchain_obj
        
        temp=[]
        for args in sys.argv:
            temp.append(args)
        
        if len(temp) == 3:
            settings.APP_URL='http://'+temp[-1]+'/'

        if( 'runserver' in temp ):
            blockchain_obj=myBlockchain()
            blockchain_obj.deployContract()
            system('')
            print(u"\u001b[32;1mSmart contract Deployed Successfully...... \u001b[0m")