from email.headerregistry import Address
from django.shortcuts import redirect, render
from adminapp.models import Candidate
from .models import *
from django.contrib.auth.models import User as BasicUser


def home(request):
    return render(request, "home.html")

def userlogin (request):
    
    return render (request, "userlogin.html")

def userlogin_process (request, id):        #id = BasicUser.id 
    gotname = request.POST.get('name')
    gotsex = request.POST.get('sex')
    gotbirth = request.POST.get('birth')
    gotaddress = request.POST.get('address')
    gotpassword = request.POST.get('password')
    searchBasicUser = BasicUser.objects.filter(id = id)
    searchuser = useraccount.objects.filter(name = gotname, sex = gotsex, birth = gotbirth, address = gotaddress, password = gotpassword)
    seacrhlogineduseraccount = logineduseraccount.objects.filter(name = gotname, sex = gotsex, birth = gotbirth, address = gotaddress, password = gotpassword)

    if seacrhlogineduseraccount.exists():        #user가 전에 로그인한 적이 있으면
        print("user have logged in before")
    else:       #user가 전에 로그인한 적이 없으면 
        new_logineduseraccount = logineduseraccount()        
        new_logineduseraccount.related_useraccount = searchBasicUser[0]
        new_logineduseraccount.name = gotname
        new_logineduseraccount.sex = gotsex
        new_logineduseraccount.birth = gotbirth
        new_logineduseraccount.address = gotaddress
        new_logineduseraccount.password = gotpassword
        new_logineduseraccount.save()
    if True:
        return redirect ('poll')
    else: 
        return redirect ('home')
    
    

def wrong (request):
    return render (request, "wrong.html")

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