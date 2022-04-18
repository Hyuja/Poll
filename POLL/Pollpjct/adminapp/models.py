from django.db import models
# Create your models here.
class Candidate(models.Model):
    CandidateNum = models.CharField (max_length = 3)
    side = models.CharField(max_length = 50)
    CandidateName = models.CharField(max_length = 20)
    votes = models.IntegerField(null = True, blank= True, default = 0)

    def __str__(self):
        return str(self.CandidateNum) + str("  ") + str(self.CandidateName)