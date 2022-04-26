from asyncore import poll
from django.shortcuts import redirect, render
import os
from urllib import parse
from .models import *
from userapp.models import *
import pandas as pd
import matplotlib as plt

def menu (request):
    return render (request, "menu.html")
#===================================================
def CandidateEdit(request):
    Candidates = Candidate.objects.all()
    return render (request, "CandidateEdit.html", {'Candidates' : Candidates})

def PollResult(request):
    if request.user.is_authenticated and request.user.is_staff:
        POLL_CASES = Poll_Cases.objects.all().order_by('poll_case_num')
        Candidates = Candidate.objects.all().order_by('Poll_Case_id')
        
        alllst = Candidate.objects.filter(id = -1)
        for pollcase in POLL_CASES:
            canlst = Candidate.objects.filter(id = -1)
            canlst = canlst | Candidate.objects.filter(Poll_Case_id = pollcase.id).order_by('-votes')       #votes 올림차순. canlst[0]이 최다득표임 
            alllst = alllst | canlst

        
        
        return render (request, "PollResult.html", {"POLL_CASES" : POLL_CASES, "alllst" : alllst})
    else:
        return redirect ('accessdenied')

def accessdenied (request):
    return render (request, 'accessdenied.html')

