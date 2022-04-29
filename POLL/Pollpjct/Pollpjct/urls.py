from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from adminapp import views as adv
from userapp import views as usv
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #admin
    path('admin/', admin.site.urls, name = "admin"),
    
    #allauth 
    path('accounts/', include('allauth.urls')),    
    
    #userapp
    path('', usv.home, name ="home"),       #버튼 누르면 로그인으로 가는 페이지
    path('signin/', usv.userlogin, name = "userlogin"),     #Template O / 위에서 버튼 눌렀을떄 가는 페이지
    path('poll/', usv.userlogin_process, name = "poll"),
    path('poll/pages=<str:id>', usv.poll_detail, name = "poll_detail"),
    path('pollprocess/<str:id>', usv.pollprocess, name = "pollprocess"),        #Template X, Redirect 'end'/ 투표 로직 
    path('end/', usv.end, name = "end"),        #사진까지 다 찍고 투표 끝났을떄 
    path('alreadyvoted/', usv.alreadyvoted, name = "alreadyvoted"),
    path('wrong/', usv.wrong, name = "wrong"),       #Template O /로그인 실패하면 가는 페이지
    path('deletewronginfo/', usv.deletewronginfo, name = "deletewronginfo"),
    path('fileupload/', usv.fileUpload, name = "fileupload"),
    path('notrequired/', usv.notrequired, name = "notrequired"),

    #adminapp
    path('adminaccess/PollResult', adv.PollResult, name = "PollResult"),         #Template O / Poll Result Visualization 
    path('adminaccess/PollResult/chart<str:id>', adv.chart, name = "chart"),
    path('adminaccess/accessdenied', adv.accessdenied, name = "accessdenied"),
    
    ####제발 지워라 
    path('example/', usv.example, name = "example"),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
