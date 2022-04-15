from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class useraccount (AbstractBaseUser):
    votername = models.CharField(max_length = 20)       #여기서부터 
    sex = models.CharField(max_length = 1)
    birth = models.DateField()
    address = models.CharField(max_length = 100)
    password = models.CharField(max_length = 12)        #여기까지는 로그인 할떄 유저가 입력하는 부분 


    ifvoted = models.BooleanField(default = False)      #여기서부터
    voteresult = models.CharField(max_length = 1, default = "0")
    etc = models.TextField(null = True, blank = True)
    is_active = models.BooleanField(default = False)
    is_admin = models.BooleanField(default = False)     #여기까지는 유저가 엑세스 X 

    USERNAME_FIELD = 'votername'
    REQIRED_FIELDS = ['votername', 'sex', 'birth', 'address', 'votesn']     #로그인창에서 받는 요소들 

    def __str__(self):
        if (self.ifvoted == True): iv = "O"
        else: iv = "X"
        return str(self.votername) +" / "+ str(self.birth)+" / "+ str(iv)   #이성준 2004-05-21, 동명이인 구분



    