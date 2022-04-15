Poll_pre : 구상 단계에 만든 기능 없는 프로젝트 


ㄴ pollpjct : userapp, adminapp 구조로 구성 


ㄴ pollpjct2 : userapp, adminapp 로그인 기능 (django.contrib.auth 아니고 자체 구현한 간단한 로그인 기능) <br/> <br/>  
reference : 참고자료


ㄴ 112269075.5.jpg : 투표 결과 지역별 시각화 예시 


ㄴ 선거인명부 서식.pdf : 선거인명부 DB 구성 예시<br/> <br/>  


pollpjct1.pdf : 기획 단계 1차 스케치 (* Diagram 막 그림, 악필, 무질서함 *)<br/> 


pollpjct2.pdf : 기획 단계 2차 스케치<br/>  


poll.pages : 기획 단계 메모 (오프라인으로 할지 온라인으로 할지 둘 차이, 공통점, 기능, etc)<br/> <br/>  <br/> <br/>  


### D1 2022/3/20~3/30 : 기획 
* 기능, 구조, etc (userapp, adminapp, pollpjct하고 함수 이름 정도) <br/> <br/>  

### D2 2022/4/12 : userapp, adminapp 로그인 (기능 X (userapp/models.py 커스텀 유저 모델만 조금), 템플릿 O)
* userapp/templates/home.html : 사진 & 버튼(누르면 userlogin으로 넘어감) <br/><br/>
<img width="900" alt="Screen Shot 2022-04-13 at 4 15 16" src="https://user-images.githubusercontent.com/96364048/163037821-9125e3bf-b867-4c26-8408-b762a69a8491.png"><br/><br/>
* adminapp/templates/adminlogin.html : (아직 로그인 요소(?) 수정 X, 이메일, pw만 있음) 
* userapp/templates/userlogin.html : 유저 로그인창 (이름, 성별, 생년월일, 주소, 등재번호)<br/><br/>
<img width="900" alt="Screen Shot 2022-04-13 at 5 02 37" src="https://user-images.githubusercontent.com/96364048/163044169-505a3175-3104-4c40-9b03-ffff1c74c7db.png"><br/><br/>
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
에서 상속받은 클래스끼리 겹친게 있었는지 MRO 발생 <br/><br/>
### D3 2022/04/13 : adminapp/model.py Candidate class, adminapp(admin X) 로그인 후 메뉴창 구현 (세부 메뉴는 뼈대만), class useraccount 수정, Excel 예시 만들기, userapp 커스텀 authenticate (안됨 ㅠ), 로그인 성공하면 logined.html, 실패하면 wrong.html <br/><br/>

### D4 2022/04/14 : adminapp CandidateEdit 기능 구현 (후보 등록, 삭제, 수정), 디자인 X 나중에 수정, adminapp/userapp 로그인 기능 구현 '시도' <br/><br/>
- templates/CandidateEdit/edit, CandidateEdit_deleted 은 id 잘 받아서 삭제도 문제없이 되는데 같은(일단 내가보기엔) 방식으로 받은 CadndidateEdit_edit은 수정 버튼 누르면 Field 'id' expected a number but got 'process*'이 번갈아가면서 나오는데 id를 int형으로 못받는듯... 근데 같은 방식으로 id 주고 받는 CandidateEdit_delete는 잘 됨
<br/><br/>

CandidateEdit.html
<img width="900" alt="Screen Shot 2022-04-15 at 12 54 25" src="https://user-images.githubusercontent.com/96364048/163515726-d6043e85-9fd8-44d4-80ef-385e300cb801.png">
 
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
