from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, "home.html")

def userlogin (request):
    return render (request, "userlogin.html")

def login_view(request):
    if (request.method == 'POST'):
        form = AuthenticationForm(request=request, data = request.POST)
        if (form.is_valid()):
            DBvotername = form.cleaned_data.get("votername")
            DBsex = form.cleaned_data.get("sex")
            DBbirth = form.cleaned_data.get("birth")
            DBaddress = form.cleaned_data.get("address")
            DBpassword = form.cleaned_data.get("votesn")
            print(DBvotername)
            print(DBpassword)
            user = authenticate(request = request, votername = DBvotername, sex = DBsex, birth = DBbirth, address = DBaddress, password = DBpassword)
            if user is not None: 
                login(request, user)
        
        return redirect('logined')
    
    else:
        form = AuthenticationForm()
        return render(request, 'wrong.html')

#     votername = models.CharField(max_length = 20)
#     sex = models.CharField(max_length = 1)
#     birth = models.DateField()
#     address = models.CharField(max_length = 100)
#     password = models.CharField(max_length = 12)
#     ifvoted = models.BooleanField(default = False)
#     voteresult = models.CharField(max_length = 1, default = "0")
#     etc = models.TextField(null = True, blank = True)
def logout_view(request):
    logout(request)
    return redirect('home')

def logined (request):
    #messages.error(request, 'LOGIN FAILED')
    return render(request, 'logined.html')