from pyexpat import model
from django.db import models
# from datetime import datetime
# from django.utils import timezone


class Poll_Cases(models.Model):
    poll_case_num = models.CharField(max_length = 3)
    # pub_date = models.DateTimeField('date published')
    poll_name = models.CharField(max_length = 100, null = True, blank = True, default = "")
    poll_status = models.BooleanField(null = True, blank = True, default = True)
    
    def __str__(self):
        return str(self.poll_case_num) + (" | ") + str(self.poll_name)

    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

class Candidate(models.Model):
    Poll_Case_id = models.ForeignKey(Poll_Cases, on_delete = models.CASCADE, default = '')
    #PROTECT : votes가 바라보고 있는 ForeignKeyField가 삭제되면 해당 요소가 같이 삭제되지 않도록 protected error를 발생시킨다 
    CandidateNum = models.CharField (max_length = 3)
    side = models.CharField(max_length = 50)
    CandidateName = models.CharField(max_length = 20)
    votes = models.IntegerField(null = True, blank = True, default = 0)

    def __str__(self):
        return str(self.CandidateNum) + (" | ") + str(self.side) + (" | ") + str(self.CandidateName) 
