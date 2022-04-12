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
에서 상속받은 클래스끼리 겹친게 있었는지 MRO 발생 

