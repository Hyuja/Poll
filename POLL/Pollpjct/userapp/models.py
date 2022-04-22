from tkinter import CASCADE
from django.db import models
from datetime import datetime
from django.utils import timezone
from adminapp.models import *
from django.contrib.auth.models import User as BasicUser

class useraccount (models.Model):
    poll_case = models.ForeignKey(Poll_Cases, on_delete = models.CASCADE, default = '')
    name = models.CharField(max_length = 20)       
    sex = models.CharField(max_length = 1)
    birth = models.DateField()
    address = models.CharField(max_length = 100)
    password = models.CharField(max_length = 120)       
    ifvoted = models.BooleanField(default = False)      
    voteresult = models.CharField(max_length = 1, default = "0")
    etc = models.TextField(null = True, blank = True)
    #pub_date = models.DateTimeField('date published',  null = True, blank = True)

    class Meta:
        pass


class logineduseraccount (models.Model):
    related_useraccount = models.ForeignKey(BasicUser, on_delete = models.CASCADE, default = '')
    name = models.CharField(max_length = 20)       
    sex = models.CharField(max_length = 1)
    birth = models.DateField()
    address = models.CharField(max_length = 100)
    password = models.CharField(max_length = 120)       

