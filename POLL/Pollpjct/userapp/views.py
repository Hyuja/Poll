from django.shortcuts import redirect, render
from adminapp.models import Candidate
from .models import *
from django.contrib.auth.models import User as BasicUser
from django.contrib import messages

def home(request):
    return render(request, "home.html")

def userlogin (request):
    return render (request, "userlogin.html")

def userlogin_process (request, id):        #id = BasicUser.id 
    POLL_CASES = Poll_Cases.objects.all().order_by('poll_case_num')     #1번 선거 케이스부터 정렬
    Candidates = Candidate.objects.all().order_by('CandidateNum')       #1번 후보부터 정렬
    gotname = request.POST.get('name')
    gotsex = request.POST.get('sex')
    gotbirth = request.POST.get('birth')
    gotaddress = request.POST.get('address')
    gotpassword = request.POST.get('password')

    searchBasicUser = BasicUser.objects.filter(id = id)     #admin에 있는 기본 유저 모델
    searchuser = useraccount.objects.filter(name = gotname, sex = gotsex, birth = gotbirth, address = gotaddress, password = gotpassword)       #명부
    seacrhlogineduseraccount = logineduseraccount.objects.filter(name = gotname, sex = gotsex, birth = gotbirth, address = gotaddress, password = gotpassword)      #입력한 정보로 만든 모델, BasicUser를 foreignkey로 가짐

    if seacrhlogineduseraccount.exists():        #user가 전에 로그인한 적이 있으면
        print("user have logged in before")
        if searchuser[0].ifvoted == False:      #그리고 유저가 투표권이 있으면
            return render (request, 'poll.html', {'POLL_CASES' : POLL_CASES, 'Candidates' : Candidates, 'searchuser' : searchuser[0]})       #저장 안하고 바로 투표화면으로 넘어가기
        else:
            return redirect ('home')

    else:       #user가 전에 로그인한 적이 없으면 
        new_logineduseraccount = logineduseraccount()        
        new_logineduseraccount.related_useraccount = searchBasicUser[0]
        new_logineduseraccount.name = gotname
        new_logineduseraccount.sex = gotsex
        new_logineduseraccount.birth = gotbirth
        new_logineduseraccount.address = gotaddress
        new_logineduseraccount.password = gotpassword
        new_logineduseraccount.save()
    
        if searchuser[0].ifvoted == False:      #그리고 유저가 투표권이 있으면
            return render (request, 'poll.html', {'POLL_CASES' : POLL_CASES, 'Candidates' : Candidates, 'searchuser' : searchuser[0]})       
        else:
            return redirect ('home')


def wrong (request):
    return render (request, "wrong.html")

def pollprocess(request):       
    return redirect ('end')

def end (request):
    return render (request, 'end.html')