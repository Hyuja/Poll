from django.contrib import admin
from django.urls import path
from adminapp import views as adv
from userapp import views as usv


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', usv.home, name ="home"),
    path('signin/', usv.userlogin, name = "userlogin")
    #path('adminaccess/', adv.login, name = "adminlogin"),
]
