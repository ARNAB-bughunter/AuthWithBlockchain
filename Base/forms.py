from django import forms
from .models import productDetail

class productDetailForm(forms.ModelForm):
	class Meta:
		model=productDetail
		fields=['productName','productDescription','image']
		
		widgets={
		'productName':forms.Textarea(attrs={'type':'textarea','rows':'2','class':'form-control','placeholder':"Enter Your Product Name",'required':'true'}),
		'productDescription':forms.Textarea(attrs={'type':'textarea','rows':'2','class':'form-control','placeholder':"Enter Your Product Description",'required':'true'}),
		'image':forms.FileInput(attrs={'id':'inputGroupFile01','class':'form-control'})
		}


		labels={
		'productName':'',
		'productDescription':'',
		'image':'',
		}

		
