"""pollpjct2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from adminapp import views as adv
from userapp import views as usv
from homeapp import views as hv

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', hv.home, name = "home"),

    path('adminlogin/', adv.adminlogin, name ="adminlogin"),
    path('adminlogin/adminlogined', adv.adminlogined, name = "adminlogined"),
    path('adminlogin/adminsignup', adv.adminsignup, name = "adminsignup"),
    path('adminlogin/newadmin', adv.newadmin, name= "newadmin"),

    path('userlogin/', usv.userlogin, name = "userlogin"),
]
