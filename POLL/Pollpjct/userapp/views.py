from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, "home.html")

def userlogin (request):
    return render (request, "userlogin.html")

def wrong (request):
    return render (request, "wrong.html")

def login_view(request):
    if (request.method == 'POST'):
        form = AuthenticationForm(request = request, data = request.POST)
        if(form.is_valid()):
            inputvotername = form.cleaned_data.get("votername")
            inputsex = form.cleaned_data.get("sex")
            inputbirth = form.cleaned_data.get("birth")
            inputaddress = form.cleaned_data.get("address")
            inputpassword = form.cleaned_data.get("votesn")
            print(inputvotername)
            print(inputpassword)
            print(inputbirth)
            
            user = authenticate(request = request, votername = inputvotername, sex = inputsex, birth = inputbirth, address = inputaddress, password = inputpassword)
            if user is not None: 
                login(request, user)
                return redirect('logined')

            else:
                form = AuthenticationForm()
                return redirect('wrong')

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