from django.shortcuts import redirect, render
from adminapp.models import Candidate
from .models import *
from .forms import *
from django.contrib.auth.models import User as BasicUser
from django.contrib import messages
from django.contrib.auth import logout
##request.user.is_authenticated

def home(request):
    return render(request, "home.html")

def userlogin (request):
    if request.user.is_authenticated:       
        userid = request.user.id
        srcBasicUser = BasicUser.objects.filter(id = userid)        #무조건 있음. 오류X / 1
        srclogied = logineduseraccount.objects.filter(related_useraccount = srcBasicUser[0].id)        #대응되는 정보. 정보입력헀으면 있음 / 2
        if srclogied.exists():      #전에 정보입력한 적이 있으면 
            gotname = srclogied[0].name
            gotsex = srclogied[0].sex
            gotbirth = srclogied[0].birth
            gotaddress = srclogied[0].address
            gotpassword = srclogied[0].password
            srcuseraccount = useraccount.objects.filter(name = gotname, sex = gotsex, birth = gotbirth, address = gotaddress, password = gotpassword, ifvoted = False)       #srclogined에 매치되는 명부 / 투표권 있는 명부만 불러옴 / 3
            
            POLL_CASE = Poll_Cases.objects.filter(id = -1)     #빈 쿼리셋 타입 가올려고
            candidate = Candidate.objects.filter(id = -1)
            
            #투표권 있는 poll_case와 그에 대응하는 candidate만 넘겨주기
            for srcus in srcuseraccount:
                POLL_CASE = POLL_CASE | Poll_Cases.objects.filter(id = srcus.poll_case.id)
            
            for pollcase in POLL_CASE:
                candidate = candidate | Candidate.objects.filter(Poll_Case_id = pollcase.id)
            
            POLL_CASE = POLL_CASE.order_by('poll_case_num')
            candidate = candidate.order_by('CandidateNum')
            if srcuseraccount.exists():    #투표권 있는 대응되는 명부 있으면 
                return render (request, 'poll.html', {'POLL_CASES' : POLL_CASE, 'Candidates' : candidate, 'searchuser' : srcuseraccount})       
            
            else:       
                return redirect('alreadyvoted')
        else: 
            return render(request, "userlogin.html")

    else:     #아예 로그인안한 상태면
        return redirect('home')

def userlogin_process (request):        #id = BasicUser.id  / 여기 접근하는 케이스는 처음 로그인 하는 상황. 그냥 정보 저장하면 됨 
    if request.user.is_authenticated:
        userid = request.user.id
        srcBasicUser = BasicUser.objects.filter(id = userid)        #무조건 있음. 오류X / 1

        gotname = request.POST.get('name').strip()
        gotsex = request.POST.get('sex').strip()
        gotbirth = request.POST.get('birth').strip()
        gotaddress = request.POST.get('address').strip()
        gotpassword = request.POST.get('password').strip()

        new_logined = logineduseraccount()
        new_logined.related_useraccount = srcBasicUser[0]
        new_logined.name = gotname
        new_logined.sex = gotsex
        new_logined.birth = gotbirth
        new_logined.address = gotaddress
        new_logined.password = gotpassword
        new_logined.save()
        
        srclogied = logineduseraccount.objects.filter(name = gotname, sex = gotsex, birth = gotbirth, address = gotaddress, password = gotpassword)     #방금 만든 거, 정보 입력한거          #대응되는 정보. 정보입력헀으면 있음 / 2
        print(srclogied[0].name)
        print(srclogied[0].password)
        #애는 인당 하나씩 있음 
        newname = srclogied[0].name
        newsex = srclogied[0].sex
        newbirth = srclogied[0].birth
        newaddress = srclogied[0].address
        newpassword = srclogied[0].password
        
        srcuseraccount = useraccount.objects.filter(name = newname, sex = newsex, birth = newbirth, address = newaddress, password = newpassword)       #srcloginedㅇㅔ 매치되는 명부 / 3 / poll_case 2개 이상에 등록되어 있으면 객체 하나 아님.
        if srcuseraccount.exists() == False:        #srclogined까지 있는데 그에 매칭되는 명부가 없을때 
            return redirect('wrong')
        srcuseraccount = useraccount.objects.filter(name = newname, sex = newsex, birth = newbirth, address = newaddress, password = newpassword, ifvoted = False)       #srcloginedㅇㅔ 매치되는 명부 / 3 / poll_case 2개 이상에 등록되어 있으면 객체 하나 아님.
        if srcuseraccount.exists() == False:        #srclogined까지 있는데 ifvoted == False인게 없을 떄 
            return redirect('alreadyvoted')
        else:       #다 맞을떄 
            POLL_CASE = Poll_Cases.objects.filter(id = -1)     #빈 쿼리셋 타입 가올려고
            candidate = Candidate.objects.filter(id = -1)

            #투표권 있는 poll_case와 그에 대응하는 candidate만 넘겨주기
            for srcus in srcuseraccount:    
                POLL_CASE = POLL_CASE | Poll_Cases.objects.filter(id = srcus.poll_case.id)

            for pollcase in POLL_CASE:
                candidate = candidate | Candidate.objects.filter(Poll_Case_id = pollcase.id)
                
            POLL_CASE = POLL_CASE.order_by('poll_case_num')
            candidate = candidate.order_by('CandidateNum')

            return render (request, 'poll.html', {'POLL_CASES' : POLL_CASE, 'Candidates' : candidate, 'searchuser' : srcuseraccount})       
            
    else: 
        return redirect('home')

def pollprocess(request, id):
    if request.user.is_authenticated:
        gotlst = request.POST['choice']
        choicelst = list(map(int, gotlst.split()))        #Candidate id 
        print(choicelst)
        userid = request.user.id
        srcBasicUser = BasicUser.objects.filter(id = userid)
        srclogined = logineduseraccount.objects.filter(related_useraccount = srcBasicUser[0].id)
        srcuseraccount = useraccount.objects.filter(name = srclogined[0].name, sex = srclogined[0].sex, birth = srclogined[0].birth, address = srclogined[0].address, password = srclogined[0].password, ifvoted = False)
        #표 늘어나는 과정 & ifvoted = True
        chosenCandidate = Candidate.objects.filter(id = -1)
        if srcuseraccount.exists():
            for p in choicelst:
                chosenCandidate = chosenCandidate | Candidate.objects.filter(id = p)

            for q in range(0, len(chosenCandidate), 1):
                chosenpollcase = Poll_Cases.objects.filter(id = -1)
                chosenCandidate[q].votes  = chosenCandidate[q].votes + 1
                chosenCandidate[q].save()  
                chosenpollcase = chosenCandidate[q].Poll_Case_id
                votedusc = useraccount.objects.filter(name = srclogined[0].name, sex = srclogined[0].sex, birth = srclogined[0].birth, address = srclogined[0].address, password = srclogined[0].password, ifvoted = False, poll_case = chosenpollcase)
                votedus = votedusc[0]
                votedus.ifvoted = True
                votedus.voteresult = chosenCandidate[q].CandidateNum
                votedus.save()
            #몇번 투표했는지 메세지 띄워주기 
            srcPollCase = Poll_Cases.objects.filter(id = id)

            if srcPollCase[0].take_endpic:
                return redirect ('fileupload')
            else: 
                return redirect ('userlogin')
        else:
            return redirect ('alreadyvoted')
    else: 
        return redirect('home')

def poll_detail (request, id):
    if request.user.is_authenticated:
        #디테일 전달 파트 
        specPoll = Poll_Cases.objects.filter(id = id)
        specCan = Candidate.objects.filter(Poll_Case_id = specPoll[0].id).order_by('CandidateNum')

        #인증 파트 
        srcBasicUser = BasicUser.objects.filter(id = request.user.id)        #무조건 있음. 오류X / 1
        srclogied = logineduseraccount.objects.filter(related_useraccount = srcBasicUser[0].id)        #무조건 있음 오류 X
        srcuserac = useraccount.objects.filter(poll_case = specPoll[0].id, name = srclogied[0].name, sex = srclogied[0].sex, birth = srclogied[0].birth, address = srclogied[0].address, password = srclogied[0].password, ifvoted = False)        
        if srcuserac.exists():
            return render (request, "poll_deatil.html", {'pollcase' : specPoll[0], 'Candidates' : specCan})
        else:
            return redirect('wrong')
    else: 
        return redirect('home')
        
def alreadyvoted(request):
    return render (request, "alreadyvoted.html")

def wrong (request):
    return render (request, "wrong.html")

def deletewronginfo(request):
    userid = request.user.id
    srcBasicUser = BasicUser.objects.filter(id = userid)
    todellogined = logineduseraccount.objects.filter(related_useraccount = srcBasicUser[0].id)      
    todellogined.delete()       #정보가 맞든 틀리든 대응되는 객체가 있기만 해도 정보입력을 할 수 없게 위에서 해놓아서 지워야 정보입력까지 도달 가능 
    return redirect ('userlogin')#

    return render(request, "example.html")

def fileUpload(request):
    if request.user.is_authenticated:            
        if request.method == "POST":        #POST or POST.get
            srcBasicUser = BasicUser.objects.filter(id = request.user.id)
            srclogined = logineduseraccount.objects.filter(related_useraccount = srcBasicUser[0])
            related_loginedaccount = srclogined[0]
            title = request.POST['title']
            img = request.FILES['imgfile']
            fileupload = logineduserpic(
                related_loginedaccount = related_loginedaccount,
                title = title,
                imgfile = img,
            )
            fileupload.save()
            return redirect ('home')

        else:
            fileuploadForm  = FileUploadForm
            context = {
                'fileuploadForm' : fileuploadForm,
            }
            return render(request, 'fileupload.html', context)
    else: 
        return redirect('home')

def notrequired(request):
    return render (request, 'notrequired.html')

def end (request):
    if request.user.is_authenticated:
        logout(request)
        return render (request, 'end.html')

    else:
        return redirect ('home')