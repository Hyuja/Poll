from django.shortcuts import render

def userlogin(request):
    return render(request, 'userlogin.html')
