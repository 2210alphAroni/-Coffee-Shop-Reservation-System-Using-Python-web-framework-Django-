from django.contrib import admin
from django.contrib.admin.sites import site
from header.models import All

# Register your models here.

class AllAdmin(admin.ModelAdmin):
    list_display=('title','favicon','logotext1','logoimg','logotext2','nav1','nav2','nav3','nav4','nav5','nav6')

admin.site.register(All,AllAdmin)
