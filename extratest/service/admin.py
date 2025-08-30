from django.contrib import admin
from django.contrib.admin.sites import site
from service.models import Redirect,Serviceinfo,Listinfo

# Register your models here.

class RedirectAdmin(admin.ModelAdmin):
    list_display=('title','nav1','slash','nav2')
admin.site.register(Redirect,RedirectAdmin)

class ServiceinfoAdmin(admin.ModelAdmin):
    list_display=('type','title')

admin.site.register(Serviceinfo,ServiceinfoAdmin)

class ListinfoAdmin(admin.ModelAdmin):
    list_display=('img','list')

admin.site.register(Listinfo,ListinfoAdmin)