from django.shortcuts import redirect, render

def home(request):
    return render(request, "home.html")

def userlogin (request):
    return render (request, "userlogin.html")

def userloginprocess (request):
    
    if (True):
        return redirect()

    else:
        return redirect("wrong.html")