from django.contrib import admin
from django.urls import include, path
from adminapp import views as adv
from userapp import views as usv


urlpatterns = [
    path('admin/', admin.site.urls, name = "admin"),

    path('', usv.home, name ="home"),       #버튼 누르면 로그인으로 가는 페이지
    path('signin/', usv.userlogin, name = "userlogin"),     #Template O / 위에서 버튼 눌렀을떄 가는 페이지
    #path('signinprocess/', usv.login_view, name = "loginprocess"),      
    path('logined/', usv.logined, name = "logined"),        #Template O / 로그인 됐을떄 가는 페이지
    path('wrong', usv.wrong, name = "wrong"),       #Template O /로그인 실패하면 가는 페이지
    path('poll/', usv.poll, name = "poll"),     #Template O /투표하는 페이지
    path('pollprocess/<str:id>', usv.pollprocess, name = "pollprocess"),        #Template X, Redirect 'end'/ 투표 로직 
    path('end/', usv.end, name = "end"),        #사진까지 다 찍고 투표 끝났을떄 

    path('adminaccess/', adv.adminloigin, name = "adminlogin"),     #Template O /어드민 홈 페이지, 어드민은 로그인부터 
    path('kakaologin/', adv.kakao_login, name = "kakaologin"),
    path('adminaccess/menu', adv.menu, name = "menu"),      #Template O / 로그인해야 접근 가능한 메뉴창, 후보 수정 등록, DB<->Excel, 통계, 시각화 등 
    path('adminaccess/CandidateEdit', adv.CandidateEdit, name = "CandidateEdit"),       #Template O / 메뉴에서 접근 
    path('adminaccess/PollResult', adv.PollResult, name = "PollResult"),         #Template O / Poll Result Visualization 
    
]
