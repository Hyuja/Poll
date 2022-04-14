from django.contrib import admin
from django.urls import path
from adminapp import views as adv
from userapp import views as usv


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', usv.home, name ="home"),
    path('signin/', usv.userlogin, name = "userlogin"), 
    path('signinprocess/', usv.login_view, name = "loginprocess"),
    path('logined/', usv.logined, name = "logined"),

    path('adminaccess/', adv.adminloigin, name = "adminlogin"),
    path('adminaccess/menu', adv.menu, name = "menu"),
    path('adminaccesss/CandidateEdit', adv.CandidateEdit, name = "CandidateEdit"),
    path('adminaccess/ExceltoDB', adv.ExceltoDB, name = "ExceltoDB"),
    path('adminaccess/DBtoExcel', adv.DBtoExcel, name = "DBtoExcel"),
    path('adminaccess/PollResult', adv.PollResult, name = "PollResult"),
]
