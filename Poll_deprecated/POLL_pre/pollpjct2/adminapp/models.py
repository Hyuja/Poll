from email.headerregistry import Address
from django.db import models

class accountinfo(models.Model):
    iid = models.CharField(max_length=20)
    pw = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    # sex = models.CharField(max_length=10)
    # address = models.CharField(max_length=250)
    # name = models.CharField(max_length=30)
    # pollsn = models.IntegerField()
    # birth = models.IntegerField()
    # pollstatus = models.BooleanField()
    # etc = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.iid
    
