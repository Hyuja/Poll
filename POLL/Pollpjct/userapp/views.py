from django.shortcuts import redirect, render
from adminapp.models import Candidate
from .models import *
from django.contrib.auth.models import User as BasicUser
from django.contrib import messages
from django.contrib.auth import logout
##request.user.is_authenticated

def home(request):
    return render(request, "home.html")

def userlogin (request):
    if request.user.is_authenticated:       
    
        POLL_CASES = Poll_Cases.objects.all().order_by('poll_case_num')     #1번 선거 케이스부터 정렬
        Candidates = Candidate.objects.all().order_by('CandidateNum')       #1번 후보부터 정렬
        userid = request.user.id
        srcBasicUser = BasicUser.objects.filter(id = userid)        #무조건 있음. 오류X / 1
        srclogied = logineduseraccount.objects.filter(related_useraccount = srcBasicUser[0].id)        #대응되는 정보. 정보입력헀으면 있음 / 2
        if srclogied.exists():      #전에 정보입력한 적이 있으면 
            gotname = srclogied[0].name
            gotsex = srclogied[0].sex
            gotbirth = srclogied[0].birth
            gotaddress = srclogied[0].address
            gotpassword = srclogied[0].password
            srcuseraccount = useraccount.objects.filter(name = gotname, sex = gotsex, birth = gotbirth, address = gotaddress, password = gotpassword)       #srcloginedㅇㅔ 매치되는 명부 / 3
            if srcuseraccount[0].ifvoted == False:      #다 됐고 투표권도 있을때
                return render (request, 'poll.html', {'POLL_CASES' : POLL_CASES, 'Candidates' : Candidates, 'searchuser' : srcuseraccount[0]})       
            elif srcuseraccount[0].ifvoted == True:     #다 됐는데 이미 투표 했을때 
                return redirect('alreadyvoted')
        
        else: 
            return render(request, "userlogin.html")

    else:     #아예 로그인안한 상태면
        return redirect('home')

def userlogin_process (request):        #id = BasicUser.id  / 여기 접근하는 케이스는 처음 로그인 하는 상황. 그냥 정보 저장하면 됨 
    if request.user.is_authenticated:
        POLL_CASES = Poll_Cases.objects.all().order_by('poll_case_num')     #1번 선거 케이스부터 정렬
        Candidates = Candidate.objects.all().order_by('CandidateNum')       #1번 후보부터 정렬
        userid = request.user.id
        srcBasicUser = BasicUser.objects.filter(id = userid)        #무조건 있음. 오류X / 1

        gotname = request.POST.get('name')
        gotsex = request.POST.get('sex')
        gotbirth = request.POST.get('birth')
        gotaddress = request.POST.get('address')
        gotpassword = request.POST.get('password')

        new_logined = logineduseraccount()
        new_logined.related_useraccount = srcBasicUser[0]
        new_logined.name = gotname
        new_logined.sex = gotsex
        new_logined.birth = gotbirth
        new_logined.address = gotaddress
        new_logined.password = gotpassword
        new_logined.save()
        
        srclogied = logineduseraccount.objects.filter(name = gotname, sex = gotsex, birth = gotbirth, address = gotaddress, password = gotpassword)     #방금 만든 거         #대응되는 정보. 정보입력헀으면 있음 / 2
        
        newname = srclogied[0].name
        newsex = srclogied[0].sex
        newbirth = srclogied[0].birth
        newaddress = srclogied[0].address
        newpassword = srclogied[0].password
        
        srcuseraccount = useraccount.objects.filter(name = newname, sex = newsex, birth = newbirth, address = newaddress, password = newpassword)       #srcloginedㅇㅔ 매치되는 명부 / 3
        
        if srcuseraccount[0].ifvoted == False:
            return render (request, 'poll.html', {'POLL_CASES' : POLL_CASES, 'Candidates' : Candidates, 'searchuser' : srcuseraccount[0]})       
        elif srcuseraccount[0].ifvoted == True:     #다 됐는데 이미 투표 했을때 
            return redirect('alreadyvoted')
    else: 
        return redirect('home')

def wrong (request):
    return render (request, "wrong.html")

def alreadyvoted(request):
    return render (request, "alreadyvoted.html")

def pollprocess(request):    
    return redirect ('end')

def end (request):
    if request.user.is_authenticated:
        logout(request)
    return render (request, 'end.html')