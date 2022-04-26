from asyncore import poll
from django.shortcuts import redirect, render
import os
from urllib import parse
from .models import *
from userapp.models import *
import pandas as pd
import matplotlib.pyplot as plt

def menu (request):
    return render (request, "menu.html")
#===================================================
def CandidateEdit(request):
    Candidates = Candidate.objects.all()
    return render (request, "CandidateEdit.html", {'Candidates' : Candidates})

def PollResult(request):
    if request.user.is_authenticated and request.user.is_staff:
        POLL_CASES = Poll_Cases.objects.all().order_by('poll_case_num')
        Candidates = Candidate.objects.all().order_by('Poll_Case_id')
        
        alllst = Candidate.objects.filter(id = -1)
        for pollcase in POLL_CASES:
            canlst = Candidate.objects.filter(id = -1)
            canlst = canlst | Candidate.objects.filter(Poll_Case_id = pollcase.id).order_by('-votes')       #votes 올림차순. canlst[0]이 최다득표임 
            alllst = alllst | canlst

        plt.rc('font', family = "NanumGothic")
        
        #선거별 투표수 총합
        allvotelst = [0] * POLL_CASES.count()       
        cnt = 0 
        for pollcase in POLL_CASES:
            candi = Candidate.objects.filter(Poll_Case_id = pollcase.id)
            for cand in candi:
                allvotelst[cnt] = allvotelst[cnt] + cand.votes
            cnt += 1
        print("총 투표수" + str(allvotelst))
        
        cntt = 0
        for pollcase in POLL_CASES:
            ratio = []      #int
            labels = []     #str
            Candi = Candidate.objects.filter(Poll_Case_id = pollcase.id)
            for candidate in Candi:
                labels.append(str(candidate.CandidateName))
                toapnd = round((candidate.votes/allvotelst[cntt])*100, 2)
                ratio.append(toapnd)
            cntt += 1 
            print(str(pollcase.poll_case_num) + " 득표율" + str(ratio))
            plt.pie(ratio, labels = labels, autopct = "%.2f%%")
            plt.show()
        
        
        return render (request, "PollResult.html", {"POLL_CASES" : POLL_CASES, "alllst" : alllst})
    else:
        return redirect ('accessdenied')

def accessdenied (request):
    return render (request, 'accessdenied.html')

