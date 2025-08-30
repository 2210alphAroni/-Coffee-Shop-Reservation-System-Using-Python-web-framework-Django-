from django.db import models

# Create your models here.

class Reservoninfo(models.Model):
    name=models.CharField(max_length=100,null=True,default=None,blank=True)
    nav1=models.CharField(max_length=100,null=True,default=None,blank=True)
    slash=models.CharField(max_length=100,null=True,default=None,blank=True)
    nav4=models.CharField(max_length=100,null=True,default=None,blank=True)
    disc=models.CharField(max_length=200,null=True,default=None,blank=True)
    online=models.CharField(max_length=100,null=True,default=None,blank=True)
    descrip=models.TextField(max_length=1000,null=True,default=None,blank=True)
    title1=models.CharField(max_length=100,null=True,default=None,blank=True)
    title2=models.CharField(max_length=100,null=True,default=None,blank=True)
    title3=models.CharField(max_length=100,null=True,default=None,blank=True)

class Table(models.Model):
    title=models.CharField(max_length=100,null=True,default=None,blank=True)
    placehol1=models.CharField(max_length=100,null=True,default=None,blank=True)
    placehol2=models.CharField(max_length=100,null=True,default=None,blank=True)
    placehol3=models.CharField(max_length=100,null=True,default=None,blank=True)
    placehol4=models.CharField(max_length=100,null=True,default=None,blank=True)
    placehol5=models.CharField(max_length=100,null=True,default=None,blank=True)
    button=models.CharField(max_length=100,null=True,default=None,blank=True)

