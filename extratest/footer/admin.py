from django.contrib import admin
from django.contrib.admin.sites import site
from footer.models import Allinfo,Designation,Signup

# Register your models here.

class AllinfoAdmin(admin.ModelAdmin):
    list_display=('title1','addr','phone','email','title2','text1','link1','link2','link3','title3','week1','shift1','week2','shift2','title4','text2','placeholder','button')
    
admin.site.register(Allinfo,AllinfoAdmin)


class DesignationAdmin(admin.ModelAdmin):
    list_display=('copyright','website','text','design','name')

admin.site.register(Designation,DesignationAdmin)

class SignupAdmin(admin.ModelAdmin):
    list_display=('id','name','email','date','time','number')
admin.site.register(Signup,SignupAdmin)