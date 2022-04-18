from django.db import models
from datetime import datetime

class useraccount (models.Model):
    name = models.CharField(max_length = 20)       
    sex = models.CharField(max_length = 1)
    birth = models.DateField()
    address = models.CharField(max_length = 100)
    password = models.CharField(max_length = 120)        
    ifvoted = models.BooleanField(default = False)      
    voteresult = models.CharField(max_length = 1, default = "0")
    etc = models.TextField(null = True, blank = True)
    pub_date = models.DateTimeField('date published', null = True, blank = True, default = datetime.now())
    
    class Meta:
        pass

    
    
