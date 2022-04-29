from django.contrib import admin
from .models import *

# Register your models here.

class noticeAdmin(admin.ModelAdmin):
    list_display = ('title','details','completed')

admin.site.register(Notice, noticeAdmin)
