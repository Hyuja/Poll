Poll_pre : 구상 단계에 만든 기능 없는 프로젝트 


ㄴ pollpjct : userapp, adminapp 구조로 구성 


ㄴ pollpjct2 : userapp, adminapp 로그인 기능 (django.contrib.auth 아니고 자체 구현한 간단한 로그인 기능) <br/> <br/>  
reference : 참고자료


ㄴ 112269075.5.jpg : 투표 결과 지역별 시각화 예시 


ㄴ 선거인명부 서식.pdf : 선거인명부 DB 구성 예시<br/> <br/>  


pollpjct1.pdf : 기획 단계 1차 스케치 (* Diagram 막 그림, 악필, 무질서함 *)<br/> 


pollpjct2.pdf : 기획 단계 2차 스케치<br/>  


poll.pages : 기획 단계 메모 (오프라인으로 할지 온라인으로 할지 둘 차이, 공통점, 기능, etc)<br/> <br/>  <br/> <br/>  


## D1 2022/3/20~3/30 : 기획 
* 기능, 구조, etc (userapp, adminapp, pollpjct하고 함수 이름 정도) 

<br/>

* * * *

<br/>

## D2 2022/4/12 : userapp, adminapp 로그인 (기능 X (userapp/models.py 커스텀 유저 모델만 조금), 템플릿 O)
* userapp/templates/home.html : 사진 & 버튼(누르면 userlogin으로 넘어감) <br/><br/>
<img width="1100" alt="Screen Shot 2022-04-13 at 4 15 16" src="https://user-images.githubusercontent.com/96364048/163037821-9125e3bf-b867-4c26-8408-b762a69a8491.png"><br/><br/>
* adminapp/templates/adminlogin.html : (아직 로그인 요소(?) 수정 X, 이메일, pw만 있음) 
* userapp/templates/userlogin.html : 유저 로그인창 (이름, 성별, 생년월일, 주소, 등재번호)<br/><br/>
<img width="1100" alt="Screen Shot 2022-04-13 at 5 02 37" src="https://user-images.githubusercontent.com/96364048/163044169-505a3175-3104-4c40-9b03-ffff1c74c7db.png"><br/><br/>
* userapp/model.py
~~~python
  from django.db import models
  from django.contrib.auth.models import AbstractBaseUser

  class useraccount (models.Model, AbstractBaseUser):
      votername = models.CharField(max_length = 20)
      sex = models.CharField(max_length = 1)
      birth = models.DateField()
      address = models.CharField(max_length = 100)
      votesn = models.CharField(max_length = 12)
      ifvoted = models.BooleanField(default = False)
      voteresult = models.CharField(max_length = 1, default = "0")
      etc = models.TextField(null = True, blank = True)

  def __str__(self):
      return str(self.votername) + str(self.birth)
~~~
에서 상속받은 클래스끼리 겹친게 있었는지 MRO 발생 

<br/>

* * * *

<br/>

## D3 2022/04/13 : adminapp/model.py Candidate class, adminapp(admin X) 로그인 후 메뉴창 구현 (세부 메뉴는 뼈대만), class useraccount 수정, Excel 예시 만들기, userapp 커스텀 authenticate (안됨 ㅠ), 로그인 성공하면 logined.html, 실패하면 wrong.html 
<br/>

* * * *

<br/>

## D4 2022/04/14 : adminapp CandidateEdit 기능 구현 (후보 등록, 삭제, 수정), 디자인 X 나중에 수정, adminapp/userapp 로그인 기능 구현 '시도' <br/>
- templates/CandidateEdit/edit, CandidateEdit_deleted 은 id 잘 받아서 삭제도 문제없이 되는데 같은(일단 내가보기엔) 방식으로 받은 CadndidateEdit_edit은 수정 버튼 누르면 Field 'id' expected a number but got 'process*'이 번갈아가면서 나오는데 id를 int형으로 못받는듯... 근데 같은 방식으로 id 주고 받는 CandidateEdit_delete는 잘 됨
<br/><br/>

CandidateEdit.html
<img width="1100" alt="Screen Shot 2022-04-15 at 12 54 25" src="https://user-images.githubusercontent.com/96364048/163515726-d6043e85-9fd8-44d4-80ef-385e300cb801.png">
 
CandidateEdit_edit.html
~~~~python 
<body>
    <div align = "middle">
        <h1>Candidate Edit</h1>
        <form  method="POST" action="{%url 'CandidateEdit_editprocess' Candidate.id %}">
            {% csrf_token %}
            <p>기호 : <input type="text" name= "CandidateNum" value = "{{Candidate.CandidateNum}}"></p>
            <p>정당 : <input type="text" name= "side" value = "{{Candidate.side}}"></p>
            <p>후보명 : <input type = "text" name= "CandidateName" value = "{{Candidate.CandidateName}}"></p>
            <button type="submit">SAVE {{Candidate.id}}</button>
            <br><br>
        </form>

        <form method = "POST" action = "{%url 'CandidateEdit_delete' Candidate.id %}">
            {% csrf_token %}
            <button type = "submit">DELETE</button>
        </form>
    </div>
</body>
</html>
~~~~

<br/>
adminapp/views.py

~~~~python 
def CandidateEdit(request):
    Candidates = Candidate.objects.all()
    return render (request, "CandidateEdit.html", {'Candidates' : Candidates})

def CandidateEdit_add (request):
    addedCandidate = Candidate()
    addedCandidate.CandidateNum = request.POST['CandidateNum']
    addedCandidate.side = request.POST['side']
    addedCandidate.CandidateName = request.POST['CandidateName']
    addedCandidate.votes = 0
    addedCandidate.save()
    return redirect ('CandidateEdit')

def CandidateEdit_delete (request, id):
    todeleteCandidate = Candidate.objects.get(id = id)
    todeleteCandidate.delete()
    return redirect ('CandidateEdit')

def CandidateEdit_edit (request, id):  
    toeditCandidate = Candidate.objects.get(id = id)
    return render(request, 'CandidateEdit_edit.html', {'toeditCandidate' : toeditCandidate})

def CandidateEdit_editprocess (request, kid):
    editCandidate = Candidate.objects.get(id = kid)
    editCandidate.CandidateNum = request.POST['CandidateNum']
    editCandidate.side = request.POST['side']
    editCandidate.CandidateName = request.POST['CandidateName']
    editCandidate.votes = 0
    editCandidate.save()
    return redirect ('CandidateEdit', editCandidate.id)
~~~~
<br/>

* * * *

<br/>

## D5 2022/04/15 poll 구현 (로그인 확인 아직 X), 로그인 방식, 선거인명부 생성 접근 계획 수정 <br/>
- 투표하면 <code></code> userapp/models.py <code> user.ifvoted = True, </code> : 중복투표 방지, <code>user.voteresult</code> : 통계, 시각화에서 편리하도록, <code>Candidate.votes = Candidate.votes + 1</code> 한표씩 추가, 개표는 여기서<br/><br/>
- 로그인 깔짝대다가 실패<br/><br/>
- poll.html에서 후보 수만큼 행, 라디오 버튼 만드려고 했으나 라디오 버튼 밸류 값이 for문에서 제대로 할당되지 않아 실패. 온클릭을 잘 쌈싸먹으면 될 것 같기도 
poll.html <br/>
<img width="1100" alt="Screen Shot 2022-04-17 at 6 00 37" src="https://user-images.githubusercontent.com/96364048/163691243-715e1d70-5b9f-40e6-a5a0-d1158043f12a.png">
poll.html 

~~~html
<body class="py-4">
<main>
<div align = "middle">
    <br><br><br>
  <h1 class="mt-4">POLL</h2>
</div>
  <div class="container">
  <form id="test" method = "POST" action = "{% url 'pollprocess' Candidates %}"></form>
    {%csrf_token%}
  <br>
    {% for Candidate in Candidates %}
        <div class="row row-cols-1 row-cols-md-3 gx-4" class="row row-cols-md-3 mb-3" >
        <div class="col themed-grid-col" align = "middle">{{Candidate.CandidateNum}}</div>
        <div class="col themed-grid-col" align = "middle">{{Candidate.side}}</div>
        <div class="col themed-grid-col" align = "middle">{{Candidate.CandidateName}}</div>
        <div class="form-check">
        <input class="form-check-input" type= "radio" onclick = "" value = "{{Candidate.id}}" name= "Candidate.id" id="flexRadioDefault1">
        <label class="form-check-label" for="flexRadioDefault1"></label>
        </div>
        </div>
    {% endfor %}
    <button form="test" type="submit" class="btn btn-primary btn-lg">Submit</button>
  </div>
</form>
</main>
</body>
~~~
<br/>
 * 카카오 로그인 기능 구현 거의 다 됐으나 <br/>
 
![Screen Shot 2022-04-17 at 6 30 01](https://user-images.githubusercontent.com/96364048/163691900-76f3808f-6941-4a2f-990c-590779692b9e.png) 

에러가 발생 kakao.developer 페이지와 views.py에 둘다 같은 링크까지 걸어줬지만 여전히 같은 오류가 떠서 다 지움 (+정작 원하던 성별, 이름, 전화번호 등 본인인증에 유의미한 자료들은 동의 있어도 받기 어렵게 되어있었음) 
<br/>

* * * *

<br/>

## D6 2022/04/16 : ExceltoDB, DBtoExcel 기능 구현, 어드민 구조 변경
 * 기존 계획에서는 admin 따로 adminaccess 따로 사용하려고 했으나 django admin창에서 너무도 쉽게 csv 파일을 DB로 import, export 할 수 있는 방법이 있어 어드민 구조 자체를 변경 <br/><br/>
 * 원래는 배포 또는 개조해서 사용 할 때는 admin이 아닌 adminaccess/ 링크로 따로 관리하려 했으나 csv 파일 import, export 뿐만 아니라 선거인 명부, 후보 수정에서 훨씬 편리 할 것 같아 adminaccess 전체 삭제 <br/><br/>

userapp/admin.py 
~~~python 
from django.contrib import admin
from .models import Candidate
from userapp.models import useraccount
from import_export.admin import ImportExportModelAdmin
# Register your models here
admin.site.register(Candidate)

@admin.register(useraccount)
class userdata(ImportExportModelAdmin):
    pass
~~~
<br/>
USERAPP/Useracocounts 에서 import, export
<img width="1100" alt="Screen Shot 2022-04-17 at 6 35 53" src="https://user-images.githubusercontent.com/96364048/163692094-efdefe5b-19b5-49aa-8f46-51aff24a05ec.png">
import 
<img width="1100" alt="Screen Shot 2022-04-17 at 6 36 04" src="https://user-images.githubusercontent.com/96364048/163692096-419c951f-bf2a-42a2-b152-e61ab3e4134b.png">
export
<img width="1100" alt="Screen Shot 2022-04-17 at 6 37 50" src="https://user-images.githubusercontent.com/96364048/163692097-e96baedc-cb32-47cf-ab32-612f09788716.png">

<br/>

* * * * 

<br/>

## D7 2022/04/17 : Excel <-> DB 엑셀 문제 해결
* 엑셀 파일에서 입력한 날짜 포맷이 안맞았음 20xx.xx.xx -> 20xx-xx-xx/ 엑셀 파일 저장 방식 중에 xlsx 등은 지원이 중단됨 (보안이슈라나?) / xls로 했는데 모르는 에러가 나옴 / csv로 했더니 됨 / import했던 파일 다시  import하니 같은 명부가 두번 올라감 (id만 다르고 다 같음) (근데 이러면 투표 두번한다던지 맞는 정보를 입력했는데도 multivalue로 로그인이 안되던지 하는 상황이 발생 가능)<br/><br/>
* DB 저장할떄 컨트롤 하고 싶어서 찾아보는중<br/><br/>
* ForeignKey, Admin 커스텀 공부하느라 얼마 못함 ㅠ<br/><br/>

* * * * 

<br/>

## D8 2022/04/18 : Django Admin 커스텀, poll - Candidates ont-to-many로 재구성 
* 기존 구조는 투표 케이스는 무조건 하나로 제안되어 한번의 실행에서 한번의 투표만 가능하도록 되어있었음, Poll_Cases를 ForeignKey로 지정해서 one to many의 방식으로 구성 <br/><br/>

adminapp/models.py
~~~python 
from pyexpat import model
from django.db import models
from datetime import datetime
from django.utils import timezone


class Poll_Cases(models.Model):
    poll_Case_Num = models.CharField(max_length = 3)
    pub_date = models.DateTimeField('date published')
    poll_name = models.CharField(max_length = 100, null = True, blank = True, default = "-1")

    def __str__(self):
        return str(self.poll_Case_Num) + (" | ") + str(self.poll_name)

class Candidate(models.Model):
    Poll_Case_id = models.ForeignKey(Poll_Cases, on_delete = models.DO_NOTHING)
    #PROTECT : votes가 바라보고 있는 ForeignKeyField가 삭제되면 해당 요소가 같이 삭제되지 않도록 protected error를 발생시킨다 
    CandidateNum = models.CharField (max_length = 3)
    side = models.CharField(max_length = 50)
    CandidateName = models.CharField(max_length = 20)
    votes = models.IntegerField(null = True, blank = True, default = 0)

    def __str__(self):
        return str(self.CandidateNum) + (" | ") + str(self.side) + (" | ") + str(self.CandidateName) 
~~~

<br/>
<img width="1100" alt="Screen Shot 2022-04-19 at 8 31 43" src="https://user-images.githubusercontent.com/96364048/163892895-e39859b5-d06b-4cd6-8218-d965212e55cc.png">

* 투표 수정하는 창에서 후보 추가할 수 있도록 <br/>

<img width="1100" alt="Screen Shot 2022-04-19 at 9 57 14" src="https://user-images.githubusercontent.com/96364048/163899421-2471ca23-9877-4212-9ce4-846fd7c750d3.png">

<br/>

* * * *

<br/>

## D9 2022/04/19 : pub_date, db 저장할떄 공백제거, 중복제거 하려고 했으나 실패 <br/>
* models.py 에서 바로 __init__으로 공백제거, 중복 컨트롤 하고 싶었는데 실패함<br/><br/>
* admin 창에서 db 만드는게 아니라 import 해오는 거라서 pub_date도 안됨 : excel에서 default값 입력하기도 어려움 <br/><br/>
* 둘 다 필수적인 요소라 꼭 넣을거임

<br/>

* * * * 

<br/>

## D10 2022/04/20 : allauth google login api, 만들어놨던 템플릿, 함수에 로그인 기능 더하기, logineduseraccount model만들기 <br/>
* allauth google 로그인. 일단 하긴 했는데 버튼 누르면 바로 구글 화면으로 넘어갔으면 하는데 allauth 로그인 화면 한번 거쳐서 가서 수정해줘야될듯, 로그아웃 버튼도. <br/><br/>
<img width="1100" alt="Screen Shot 2022-04-21 at 17 51 07" src="https://user-images.githubusercontent.com/96364048/164417894-19ef714c-0dc4-4449-8200-98c8f8e22917.png">

* base.html에 footer 넣어서 밑에서 계정 정보, 어드민 여부 (어드민이면 어드민 페이지로 넘어가는 버튼), 오류 신고 같은 버튼 만듦 <br/><br/>
* logineduseraccount 

<br/>

* * * * 

<br/>

## D11 2022/04/21 : 소셜로그인하고 정보입력하는 메서드 구현하고 이것저것 다 

<br/>

* * * * 

<br/>

## D12 2022/04/22 : 로그인한 이후 footer보이도록 (로그인된 계정 정보 보여주고, 로그아웃 버튼, staff이면 admin가는 버튼)

<br>

* * * *

<br/>

## D13 2022/04/23 : 자잘한 수정
<br/>

* allauth 기본 템플릿 떄문에 {% url 'google_login' %} 눌렀을 떄 <br/>

![yldp2](https://user-images.githubusercontent.com/96364048/164879284-f695ef33-ef32-458a-9b7b-b8bd54c939fa.png)

<br/>

여기에 걸려서 바로 로그인이 안되길래 settings.py에 <code>SOCIALACCOUNT_LOGIN_ON_GET = True</code> 로 해결. <br/><br/>

* 로그아웃 할 떄도 allauth 기본 템플릿에 걸리는데 그건 <code>LOGOUT_ON_GET = True</code> 로 해결.  <br/><br/>

* 로그아웃 구현<br/>

template 에서는 

~~~html
<form method="post" action="{% url 'account_logout' %}">
  {% csrf_token %}
  {% if redirect_field_value %}
    <input type="hidden" name="{{ redirect_field_name }}" value="{{ redirect_field_value }}"/>
  {% endif %}
    <button class="btn btn-outline-secondary" type="submit">Sign out</button>
</form> 
~~~ 

views.py 에서는 <br/>
<code>from django.contrib.auth import logout</code> 하고 <code>logout(request)</code> 

## D14 2022/04/24: poll.html, 로그인, 이것저것 <br/>
* poll에서 선거별, 후보별로 잘 표시 되었지만 투표권 없는 투표까지 나와서 views에서 전달할때 투표권 있는 투표만 걸러서 전달하기<br/><br/>

userapp/views.py <code>def userlogin_process</code> 중 일부
~~~python
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
~~~
~~이게되네ㅋㅋ~~
<br/><br/>
* 투표별 후보로 섞이지 않게<br/><br/>

poll.html
~~~html
{% for POLL_CASE in POLL_CASES %}
  <h1 class="mt-4">{{POLL_CASE.poll_name}}</h1><br>

  {% csrf_token %}

    {% for Candidate in Candidates %} 
      <!-- 선거별로 후보 분류 -->
        {% if Candidate.Poll_Case_id == POLL_CASE %}
          <div class="row row-cols-1 row-cols-md-3 gx-4">
            <div class="col themed-grid-col">{{Candidate.CandidateNum}}</div>
            <div class="col themed-grid-col">{{Candidate.side}}</div>
            <div class="col themed-grid-col">{{Candidate.CandidateName}}</div>
          </div>
        {% endif %}
     {% endfor %}
  <br><br><br>
{% endfor %}
~~~

결과
<img width="1100" alt="Screen Shot 2022-04-25 at 7 26 49" src="https://user-images.githubusercontent.com/96364048/164999514-973fc44f-1949-4419-9661-bdc16df04535.png">
<br/><br/>

* views.py 로그인은 너무 길어서 따로 첨부 X. 소셜로그인 -> 정보입력 인데 정보입력은 첫 로그인 때만 하도록 하게 되어 있음 -> 처음에 틀린 정보를 입력하면 계속 로그인 실패 그래서 로그인 다시 시도 버튼을 누르면 정보입력창에 다시 접근하기 위해 social account에 대응되는 틀린 정보를 아예 삭제하도록 함 <br/><br/>
~~~python 
def deletewronginfo(request):
    userid = request.user.id
    srcBasicUser = BasicUser.objects.filter(id = userid)
    todellogined = logineduseraccount.objects.filter(related_useraccount = srcBasicUser[0].id)      
    todellogined.delete()       #정보가 맞든 틀리든 대응되는 객체가 있기만 해도 정보입력을 할 수 없게 위에서 해놓아서 지워야 정보입력까지 도달 가능 
    return redirect ('userlogin')
~~~
<br/>
* 현재까지 로그인 구조(일단 아직까지는 버그 못찾음) <br/>
![KakaoTalk_Photo_2022-04-25-08-18-14](https://user-images.githubusercontent.com/96364048/165000802-a33f9dc9-8520-4bea-bd1e-5ecaa0a20ebc.jpeg)

<br/>

* * * *

<br/>

## D15 2022/04/25 : poll, poll_process 구현, 관련 기능 이것저것 <br/>
* poll에서 poll_process로 선택한 후보 id로 넘겨줄 떄 (프론트 수정 안해서 투표하려면 후보 id 입력해줘야됨) <br/>
~~poll.html 도저히 못하겠음 아니 for문에 라디오 버튼 넣었더니 그냥 다 이상해짐~~
~~~python 
gotlst = request.POST['choice']
choicelst = list(map(int, gotlst.split()))        #Candidate id 
print(choicelst)
userid = request.user.id
srcBasicUser = BasicUser.objects.filter(id = userid)
srclogined = logineduseraccount.objects.filter(related_useraccount = srcBasicUser[0].id)
srcuseraccount = useraccount.objects.filter(name = srclogined[0].name, sex = srclogined[0].sex, birth = srclogined[0].birth, address = srclogined[0].address, password = srclogined[0].password, ifvoted = False)
#표 늘어나는 과정 & ifvoted = True
chosenCandidate = Candidate.objects.filter(id = -1)

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
    votedus.save()
~~~
<br/>
* userlogin에서 poll 넘어갈 떄 아예 filter(~, ifvoted = False) 해놓아서 1, 2, 3 번 투표중에 1, 3만 하면 나중에 2 할 수 있음 (아무튼 지금까지는 버그 없고 웬만한 케이스에는 다 작동한다는 뜻) <br/><br/>
* adminaccess/PollResult 간단히 구현 
* 
