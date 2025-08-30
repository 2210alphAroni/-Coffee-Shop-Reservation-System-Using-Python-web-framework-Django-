from django.db import models

# Create your models here.

class All(models.Model):
    title=models.CharField(max_length=100,null=True,default=None,blank=True)
    favicon=models.ImageField(upload_to="",null=True,default=None,blank=True)
    logotext1=models.CharField(max_length=100,null=True,default=None,blank=True)
    logoimg=models.ImageField(upload_to="",null=True,default=None,blank=True)
    logotext2=models.CharField(max_length=100,null=True,default=None,blank=True)
    nav1=models.CharField(max_length=100,null=True,default=None,blank=True)
    nav2=models.CharField(max_length=100,null=True,default=None,blank=True)
    nav3=models.CharField(max_length=100,null=True,default=None,blank=True)
    nav4=models.CharField(max_length=100,null=True,default=None,blank=True)
    nav5=models.CharField(max_length=100,null=True,default=None,blank=True)
    nav6=models.CharField(max_length=100,null=True,default=None,blank=True)