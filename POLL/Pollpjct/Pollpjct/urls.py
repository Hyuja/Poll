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
    path('wrong', usv.wrong, name = "wrong"),

    path('adminaccess/', adv.adminloigin, name = "adminlogin"),
    path('adminaccess/menu', adv.menu, name = "menu"),
    path('adminaccess/CandidateEdit', adv.CandidateEdit, name = "CandidateEdit"),
    path('adminaccess/CandidateEdit/add', adv.CandidateEdit_add, name = "CandidateEdit_add"),
    path('adminaccess/CandidateEdit/edit<str:id>', adv.CandidateEdit_edit, name = "CandidateEdit_edit"),
    path('adminaccess/CandidateEdit/editprocess<str:id>', adv.CandidateEdit_editprocess, name = "CandidateEdit_editprocess"),
    path('adminaccess/CandidateEdit/delete<str:id>', adv.CandidateEdit_delete, name = "CandidateEdit_delete"),
    path('adminaccess/ExceltoDB', adv.ExceltoDB, name = "ExceltoDB"),
    path('adminaccess/DBtoExcel', adv.DBtoExcel, name = "DBtoExcel"),
    path('adminaccess/PollResult', adv.PollResult, name = "PollResult"),
]
