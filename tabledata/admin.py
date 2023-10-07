from django.contrib import admin
from tabledata.models import reginfo
# Register your models here.

class reginfoAdmin(admin.ModelAdmin):
    list_display=('regno','name','fname','mname','phone','address','city','gender','course','btime','photo',)
admin.site.register(reginfo,reginfoAdmin)