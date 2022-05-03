from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# @admin.action(description = "delete blank of selected accounts")
# def accountstrip(modeladmin, request, useraccount):
    

@admin.register(useraccount)
class useraccountAdmin(ImportExportModelAdmin):
    list_display = ['poll_case', 'name', 'sex', 'birth', 'address', 'password', 'etc', 'ifvoted', 'voteresult', 'id']
    actions = ['trim_data', 'offer_identical_accounts']

    def trim_data (self, request, selected):
        useraccounts = useraccount.objects.filter()
        for uscs in useraccounts:
            usc = useraccount.objects.get(id = uscs.id)
            usc.name = usc.name.strip()
            usc.sex = usc.sex.strip()
            usc.address = usc.address.strip()
            usc.password = usc.password.strip()
            usc.voteresult = usc.voteresult.strip()
            usc.save()

    def offer_identical_accounts(self, request, selected):
        pass

@admin.register(logineduseraccount)
class logineduseraccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'sex', 'birth', 'address', 'password', 'id']

@admin.register(logineduserpic)
class logineduserpicAdmin(admin.ModelAdmin):
    list_display = ['related_loginedaccount', 'title', 'imgfile']