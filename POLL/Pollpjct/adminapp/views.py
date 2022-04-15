from django.shortcuts import redirect, render
from .models import *
# Create your views here.
def adminloigin (request):
    return render(request, "adminlogin.html")

def menu (request):
    return render (request, "menu.html")

def CandidateEdit(request):
    Candidates = Candidate.objects.all()
    return render (request, "CandidateEdit.html", {'Candidates' : Candidates})

def CandidateEdit_add (request):
    addedCandidate = Candidate()
    addedCandidate.CandidateNum = request.POST['CandidateNum']
    addedCandidate.side = request.POST['side']
    addedCandidate.CandidateName = request.POST['CandidateName']
    addedCandidate.votes = 0
    addedCandidate.save()
    return redirect ('CandidateEdit')

def CandidateEdit_delete (request, id):
    todeleteCandidate = Candidate.objects.get(id = id)
    todeleteCandidate.delete()
    return redirect ('CandidateEdit')

def CandidateEdit_edit (request, id):  
    toeditCandidate = Candidate.objects.get(id = id)
    return render(request, 'CandidateEdit_edit.html', {'toeditCandidate' : toeditCandidate})

def CandidateEdit_editprocess (request, kid):
    editCandidate = Candidate.objects.get(id = kid)
    editCandidate.CandidateNum = request.POST['CandidateNum']
    editCandidate.side = request.POST['side']
    editCandidate.CandidateName = request.POST['CandidateName']
    editCandidate.votes = 0
    editCandidate.save()
    return redirect ('CandidateEdit', editCandidate.id)







def ExceltoDB(request):
    return render (request, "ExceltoDB.html")

def DBtoExcel (request):
    return render (request, "DBtoExcel.html")

def PollResult(request):
    return render (request, "PollResult.html")