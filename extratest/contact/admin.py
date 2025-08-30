from django.contrib import admin
from django.contrib.admin.sites import site
from contact.models import Continfo,Form,Conlast

# Register your models here.

class ContinfoAdmin(admin.ModelAdmin):
    list_display=('name','nav1','slash','nav6','name1','title1','title2','title3','title4','addr','phone','email','img')

admin.site.register(Continfo,ContinfoAdmin)

class FormAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','message')

admin.site.register(Form,FormAdmin)

class ConlastAdmin(admin.ModelAdmin):
    list_display=('hol1','hol2','hol3','hol4','button')

admin.site.register(Conlast,ConlastAdmin)
