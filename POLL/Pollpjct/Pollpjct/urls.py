from django.contrib import admin
from django.urls import include, path
from adminapp import views as adv
from userapp import views as usv

urlpatterns = [
    #admin
    path('admin/', admin.site.urls, name = "admin"),
    
    #allauth 
    path('accounts/', include('allauth.urls')),    
    
    #userapp
    path('', usv.home, name ="home"),       #버튼 누르면 로그인으로 가는 페이지
    path('signin/', usv.userlogin, name = "userlogin"),     #Template O / 위에서 버튼 눌렀을떄 가는 페이지
    path('poll/', usv.userlogin_process, name = "poll"),
    path('wrong/', usv.wrong, name = "wrong"),       #Template O /로그인 실패하면 가는 페이지
    path('pollprocess/', usv.pollprocess, name = "pollprocess"),        #Template X, Redirect 'end'/ 투표 로직 
    path('end/', usv.end, name = "end"),        #사진까지 다 찍고 투표 끝났을떄 
    path('alreadyvoted/', usv.alreadyvoted, name = "alreadyvoted"),
    path('deletewronginfo/', usv.deletewronginfo, name = "deletewronginfo"),
    #adminapp
    path('adminaccess/', adv.adminloigin, name = "adminlogin"),     #Template O /어드민 홈 페이지, 어드민은 로그인부터 
    path('adminaccess/PollResult', adv.PollResult, name = "PollResult"),         #Template O / Poll Result Visualization 

    
]
