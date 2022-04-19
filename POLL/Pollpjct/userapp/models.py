from django.db import models
from datetime import datetime
from django.utils import timezone
from adminapp.models import *

class useraccount (models.Model):
    name = models.CharField(max_length = 20)       
    sex = models.CharField(max_length = 1)
    birth = models.DateField()
    address = models.CharField(max_length = 100)
    password = models.CharField(max_length = 120)
    voting_rights = models.BooleanField(default = False)        
    ifvoted = models.BooleanField(default = False)      
    voteresult = models.CharField(max_length = 1, default = "0")
    etc = models.TextField(null = True, blank = True)
    pub_date = models.DateTimeField('date published')
    
    class Meta:
        pass

    
    
