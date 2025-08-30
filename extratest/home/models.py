from django.db import models

# Create your models here.

class Carousel(models.Model):
    image=models.ImageField(upload_to="",null=True,default=None,blank=True)
    title=models.CharField(max_length=150,null=True,default=None,blank=True)
    name=models.CharField(max_length=150,null=True,default=None,blank=True)
    year=models.CharField(max_length=150,null=True,default=None,blank=True)

class About(models.Model):
    type=models.CharField(max_length=150,null=True,default=None,blank=True)
    title1=models.CharField(max_length=150,null=True,default=None,blank=True)
    name1=models.CharField(max_length=150,null=True,default=None,blank=True)
    title2=models.CharField(max_length=150,null=True,default=None,blank=True)
    des1=models.TextField(max_length=1000,null=True,default=None,blank=True)
    more1=models.CharField(max_length=150,null=True,default=None,blank=True)
    image=models.ImageField(upload_to="",null=True,default=None,blank=True)
    name2=models.CharField(max_length=150,null=True,default=None,blank=True)
    des2=models.TextField(max_length=1000,null=True,default=None,blank=True)
    title3=models.CharField(max_length=150,null=True,default=None,blank=True)
    title4=models.CharField(max_length=150,null=True,default=None,blank=True)
    title5=models.CharField(max_length=150,null=True,default=None,blank=True)
    more2=models.CharField(max_length=150,null=True,default=None,blank=True)