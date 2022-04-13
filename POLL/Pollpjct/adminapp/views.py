from django.shortcuts import render

# Create your views here.
def adminloigin (request):
    return render(request, "adminlogin.html")

def menu (request):
    return render (request, "menu.html")

def CandidateEdit(request):
    return render (request, "CandidateEdit.html")

def ExceltoDB(request):
    return render (request, "ExceltoDB.html")

def DBtoExcel (request):
    return render (request, "DBtoExcel.html")

def PollResult(request):
    return render (request, "PollResult.html")