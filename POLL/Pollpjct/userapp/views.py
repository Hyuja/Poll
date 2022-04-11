from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def userlogin (request):
    return render (request, "userlogin.html")
