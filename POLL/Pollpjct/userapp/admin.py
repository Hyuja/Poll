from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# @admin.action(description = "delete blank of selected accounts")
# def accountstrip(modeladmin, request, useraccount):
    

@admin.register(useraccount)
class useraccountAdmin(ImportExportModelAdmin):
    list_display = ['poll_case', 'name', 'sex', 'birth', 'address', 'password', 'etc', 'ifvoted', 'voteresult', 'id']
    
@admin.register(logineduseraccount)
class logineduseraccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'sex', 'birth', 'address', 'password', 'id']
