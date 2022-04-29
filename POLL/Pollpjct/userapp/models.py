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
    voteresult = models.CharField(max_length = 5, null = True, blank = True, default = "")
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
    
    def __str__(self):
        return str(self.name) + (" ") + str(self.birth)

class logineduserpic (models.Model):
    related_loginedaccount = models.ForeignKey(logineduseraccount, on_delete = models.CASCADE, default = '')
    title = models.CharField(max_length = 40, null = True)
    imgfile = models.ImageField(null = True, blank = True, upload_to = "")

    def __str__(self):
        return self.title