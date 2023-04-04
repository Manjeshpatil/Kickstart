from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import authenticate,login,logout 
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
# Create your views here.


def RegisterPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
     form = CreateUserForm()
     if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
         form.save()
         user = form.cleaned_data.get('username')
         messages.success(request,'Account is created for  '+  user)
         return redirect('login')
    
    context ={'form':form}
    return render(request, "signin/register.html", context)


def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    else:
      if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'username or password is incorrect')
            
    context = {}        
    return render(request, "signin/login.html", context)




def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def HomePage(request):
    return render(request, "signin/home.html")

    