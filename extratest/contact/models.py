from django.db import models

# Create your models here.


class Continfo(models.Model):
    name=models.CharField(max_length=150,null=True,default=None,blank=True)
    nav1=models.CharField(max_length=150,null=True,default=None,blank=True)
    slash=models.CharField(max_length=150,null=True,default=None,blank=True)
    nav6=models.CharField(max_length=150,null=True,default=None,blank=True)
    name1=models.CharField(max_length=150,null=True,default=None,blank=True)
    title1=models.CharField(max_length=300,null=True,default=None,blank=True)
    title2=models.CharField(max_length=300,null=True,default=None,blank=True)
    title3=models.CharField(max_length=300,null=True,default=None,blank=True)
    title4=models.CharField(max_length=300,null=True,default=None,blank=True)
    addr=models.CharField(max_length=300,null=True,default=None,blank=True)
    phone=models.CharField(max_length=300,null=True,default=None,blank=True)
    email=models.EmailField(max_length=100,null=True,default=None,blank=True)
    img=models.ImageField(upload_to="",null=True,default=None,blank=True)

class Form(models.Model):
    name=models.CharField(max_length=150,null=True,default=None,blank=True)
    email=models.EmailField(max_length=100,null=True,default=None,blank=True)
    subject=models.CharField(max_length=150,null=True,default=None,blank=True)
    message=models.TextField(max_length=1000,null=True,default=None,blank=True)

class Conlast(models.Model):
    hol1=models.CharField(max_length=150,null=True,default=None,blank=True)
    hol2=models.CharField(max_length=150,null=True,default=None,blank=True)
    hol3=models.CharField(max_length=150,null=True,default=None,blank=True)
    hol4=models.CharField(max_length=150,null=True,default=None,blank=True)
    button=models.CharField(max_length=150,null=True,default=None,blank=True)