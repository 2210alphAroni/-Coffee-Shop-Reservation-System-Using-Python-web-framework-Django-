from django.contrib import admin
from django.contrib.admin.sites import site
from home.models import Carousel,About

# Register your models here.

class CarouselAdmin(admin.ModelAdmin):
    list_display=('image','title','name','year')

admin.site.register(Carousel,CarouselAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display=('type',
    'title1',
    'name1',
    'title2',
    'more1',
    'image',
    'name2',
    'des2',
    'title3',
    'title4',
    'title5',
    )
admin.site.register(About,AboutAdmin)
