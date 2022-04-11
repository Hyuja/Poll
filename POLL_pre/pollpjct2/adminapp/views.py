from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import accountinfo as ac


def adminlogin(request):
    return render(request, "adminlogin.html")


def adminsignup(request):
    return render (request, 'adminsignup.html')


def newadmin(request):
    new_account = ac()
    new_account.iid = request.POST['new_adminid']
    new_account.pw = request.POST['new_adminpw']
    new_account.email = request.POST['new_adminemail']
    new_account.pub_date = timezone.now()

    new_account.save()  
    return redirect('adminlogin')


def adminlogined(request):
    adminid = request.POST['adminid']
    adminpw = request.POST['adminpw']
    
    ifid = False
    ifpw = False

    allac = ac.objects.filter(iid = adminid)
    print(allac[0].pw)
    
    for p in range(0, len(allac), 1):
        if ((allac[p].iid) == (adminid)):
            ifid = True
    for q in range(0, len(allac), 1):
        if((allac[q].pw) == (adminpw)):
            ifpw = True

    if (ifid == True and ifpw == True):
        return render(request, 'adminlogined_final.html', {'adminid': adminid, 'adminpw': adminpw})

    else:
        return render(request, 'wrong.html')

