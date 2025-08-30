from django.db import models

# Create your models here.

class Menustart(models.Model):
    name=models.CharField(max_length=100,null=True,default=None,blank=True)
    home=models.CharField(max_length=100,null=True,default=None,blank=True)
    slash=models.CharField(max_length=100,null=True,default=None,blank=True)
    menu=models.CharField(max_length=100,null=True,default=None,blank=True)
    title1=models.CharField(max_length=100,null=True,default=None,blank=True)
    title2=models.CharField(max_length=100,null=True,default=None,blank=True)
    title3=models.CharField(max_length=100,null=True,default=None,blank=True)
    img=models.ImageField(upload_to="",null=True,default=None,blank=True)
    taka=models.CharField(max_length=100,null=True,default=None,blank=True)

class Category(models.Model):
    cate1=models.CharField(max_length=100,null=True,default=None,blank=True)
    cate2=models.CharField(max_length=100,null=True,default=None,blank=True)

class Pricing(models.Model):
    img=models.ImageField(upload_to="",null=True,default=None,blank=True)
    price=models.CharField(max_length=100,null=True,default=None,blank=True)
    name=models.CharField(max_length=100,null=True,default=None,blank=True)
    title=models.CharField(max_length=250,null=True,default=None,blank=True)