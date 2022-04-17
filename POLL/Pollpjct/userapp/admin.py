from django.contrib import admin
from .models import useraccount
from import_export.admin import ImportExportModelAdmin


@admin.register(useraccount)
class userdata(ImportExportModelAdmin):
    list_display = ['name', 'sex', 'birth', 'address', 'password', 'etc', 'ifvoted', 'voteresult']
    

