from django.shortcuts import redirect, render
import os
from urllib import parse
from .models import *
from userapp.models import *


def adminloigin (request):
    return render(request, "adminlogin.html")

def kakao_login (request):
    return redirect ('home')
#===================================================
def menu (request):
    return render (request, "menu.html")
#===================================================
def CandidateEdit(request):
    Candidates = Candidate.objects.all()
    return render (request, "CandidateEdit.html", {'Candidates' : Candidates})

def PollResult(request):
    return render (request, "PollResult.html")


