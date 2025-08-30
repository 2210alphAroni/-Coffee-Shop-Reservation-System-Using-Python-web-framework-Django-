from django.contrib import admin
from django.contrib.admin.sites import site
from reservation.models import Reservoninfo,Table

# Register your models here.

class ReservoninfoAdmin(admin.ModelAdmin):
    list_display=('name','nav1','slash','nav4','disc','online','descrip','title1','title2','title3')

admin.site.register(Reservoninfo,ReservoninfoAdmin)

class TableAdmin(admin.ModelAdmin):
    list_display=('title','placehol1','placehol2','placehol3','placehol4','placehol5','button')

admin.site.register(Table,TableAdmin)