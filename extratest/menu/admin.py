from django.contrib import admin
from django.contrib.admin.sites import site
from menu.models import Menustart,Category,Pricing

# Register your models here.

class MenustartAdmin(admin.ModelAdmin):
    list_display=('name','home','slash','menu','title1','title2','title3','img','taka')

admin.site.register(Menustart,MenustartAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=('cate1','cate2')

admin.site.register(Category,CategoryAdmin)

class PricingAdmin(admin.ModelAdmin):
    list_display=('img','price','name','title')

admin.site.register(Pricing,PricingAdmin)