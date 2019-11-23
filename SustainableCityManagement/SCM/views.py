from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import UserDetails
from .forms import UserLoginForm
# Create your views here.
def login_view(request):
    form = UserLoginForm(request.POST or None)        
    context = {
        'form': form
        }

    return render(request, "login.html", context)

def ValidateLoginView(request):
    userName = request.POST['userName']
    password = request.POST['password']
    userLoginDetails = UserDetails.objects.get()
    if userLoginDetails.userName == userName and userLoginDetails.Password == password:
               return render(request,"dashboard.html",{})
    else:
        return HttpResponse("Invalid username or password.")

def DisplayMapView(request):
    return render(request,"home.html",{})

    

