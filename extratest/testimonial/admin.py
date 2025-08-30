from django.contrib import admin
from django.contrib.admin.sites import site
from testimonial.models import Testiinfo

# Register your models here.

class TestiinfoAdmin(admin.ModelAdmin):
    list_display=('name','nav1','slash','nav5','name1','title1','title2','title3','click')

admin.site.register(Testiinfo,TestiinfoAdmin)