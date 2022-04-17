from django.shortcuts import redirect, render
from adminapp.models import Candidate
from .models import *

def home(request):
    return render(request, "home.html")

def userlogin (request):
    return render (request, "userlogin.html")

def wrong (request):
    return render (request, "wrong.html")

def logined (request):
    #messages.error(request, 'LOGIN FAILED')
    return render(request, 'logined.html')

def poll (request):
    Candidates = Candidate.objects.all()
    return render(request, 'poll.html', {'Candidates' : Candidates})

def pollprocess(request, id):
    gotvotedCandidate = Candidate.objects.get(id = id)
    gotvotedCandidate.votes = gotvotedCandidate.votes + 1
    #user.voteresult = gotvotedCandidate.CandidateNum
    #user.ifvoted = True
    return redirect ('end')

def end (request):
    return render (request, 'end.html')