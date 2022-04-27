from django.contrib import admin
from .models import *
from userapp.models import *


# @admin.register(Poll_Cases)
# class Poll_CasesAdmin(admin.ModelAdmin):
#     list_display = ['poll_Case_Num', 'poll_name', 'pub_date', 'id']     

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['Poll_Case_id', 'CandidateNum', 'side', 'CandidateName', 'votes', 'id']

class CandidateInline(admin.TabularInline):
    model = Candidate
    fields = ('Poll_Case_id', 'CandidateNum', 'side', 'CandidateName', 'votes')
    readonly_fields = ('CandidatePic', 'content')
    extra = 1

class Poll_CasesAdmin(admin.ModelAdmin):
    list_display = ['poll_case_num', 'poll_name', 'poll_status', 'id']     
    inlines = [CandidateInline]

admin.site.register(Poll_Cases, Poll_CasesAdmin)