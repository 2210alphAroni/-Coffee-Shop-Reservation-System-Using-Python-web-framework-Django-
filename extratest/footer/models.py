from django.db import models

# Create your models here.

class Allinfo(models.Model):
    title1=models.CharField(max_length=150,null=True,default=None,blank=True)
    addr=models.CharField(max_length=150,null=True,default=None,blank=True)
    phone=models.CharField(max_length=150,null=True,default=None,blank=True)
    email=models.EmailField(max_length=150,null=True,default=None,blank=True)
    title2=models.CharField(max_length=150,null=True,default=None,blank=True)
    text1=models.CharField(max_length=150,null=True,default=None,blank=True)
    link1=models.CharField(max_length=150,null=True,default=None,blank=True)
    link2=models.CharField(max_length=150,null=True,default=None,blank=True)
    link3=models.CharField(max_length=150,null=True,default=None,blank=True)
    title3=models.CharField(max_length=150,null=True,default=None,blank=True)
    week1=models.CharField(max_length=150,null=True,default=None,blank=True)
    shift1=models.CharField(max_length=150,null=True,default=None,blank=True)
    week2=models.CharField(max_length=150,null=True,default=None,blank=True)
    shift2=models.CharField(max_length=150,null=True,default=None,blank=True)
    title4=models.CharField(max_length=150,null=True,default=None,blank=True)
    text2=models.CharField(max_length=150,null=True,default=None,blank=True)
    placeholder=models.CharField(max_length=150,null=True,default=None,blank=True)
    button=models.CharField(max_length=150,null=True,default=None,blank=True)

class Designation(models.Model):
    copyright=models.CharField(max_length=150,null=True,default=None,blank=True)
    website=models.CharField(max_length=150,null=True,default=None,blank=True)
    text=models.CharField(max_length=150,null=True,default=None,blank=True)
    design=models.CharField(max_length=150,null=True,default=None,blank=True)
    name=models.CharField(max_length=150,null=True,default=None,blank=True)

class Signup(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=150,null=True,default=None,blank=True)
    email=models.EmailField(max_length=200,null=True,default=None,blank=True)
    date=models.DateField(null=True,default=None,blank=True)
    time=models.TimeField(null=True,default=None,blank=True)
    number=models.IntegerField(null=True,default=None,blank=True)