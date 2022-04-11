from django.shortcuts import render

def adminlogin(request):
    return render(request, "adminaccess_home.html")

def adminlogined (request): 
    adminid = request.GET['adminid']
    adminpw = request.GET['adminpw']
    return render(request, "adminaccess_logined.html", {'adminid': adminid, 'adminpw':adminpw})
    #for i in range(0,)