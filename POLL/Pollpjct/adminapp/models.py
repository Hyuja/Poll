from django.db import models
# Create your models here.
class Candidate(models.Model):
    CandidateName = models.CharField(max_length = 20)
    side = models.CharField(max_length = 50)
    CandidateNum = models.CharField (max_length = 3)
    votes = models.IntegerField()

    def __str__(self):
        return str(self.CandidateNum) + str("  ") + str(self.CandidateName)