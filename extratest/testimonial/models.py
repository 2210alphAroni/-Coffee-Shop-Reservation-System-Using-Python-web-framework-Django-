from django.db import models

# Create your models here.

class Testiinfo(models.Model):
    name=models.CharField(max_length=150,null=True,default=None,blank=True)
    nav1=models.CharField(max_length=150,null=True,default=None,blank=True)
    slash=models.CharField(max_length=150,null=True,default=None,blank=True)
    nav5=models.CharField(max_length=150,null=True,default=None,blank=True)
    name1=models.CharField(max_length=150,null=True,default=None,blank=True)
    title1=models.CharField(max_length=300,null=True,default=None,blank=True)
    title2=models.CharField(max_length=300,null=True,default=None,blank=True)
    title3=models.CharField(max_length=300,null=True,default=None,blank=True)
    click=models.CharField(max_length=100,null=True,default=None,blank=True)

