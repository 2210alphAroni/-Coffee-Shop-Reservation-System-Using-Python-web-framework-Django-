from django.db import models

# Create your models here.

class Redirect(models.Model):
    title=models.CharField(max_length=100,null=True,default=None,blank=True)
    nav1=models.CharField(max_length=100,null=True,default=None,blank=True)
    slash=models.CharField(max_length=100,null=True,default=None,blank=True)
    nav2=models.CharField(max_length=100,null=True,default=None,blank=True)

class Serviceinfo(models.Model):
    type=models.CharField(max_length=200,null=True,default=None,blank=True)
    title=models.CharField(max_length=200,null=True,default=None,blank=True)

class Listinfo(models.Model):
    img=models.ImageField(upload_to="",null=True,default=None,blank=True)
    list=models.CharField(max_length=100,null=True,default=None,blank=True)
    