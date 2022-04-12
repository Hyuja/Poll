from django.shortcuts import render

# Create your views here.
def adminloigin (request):
    return render(request, "adminlogin.html")

def menu (request):
    return render (request, "menu.html")