from django.shortcuts import render
from .forms import SignUp
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# Create your views here.


def home(request):
    return render(request,'core/home.html')

def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignUp(request.POST)
            if fm.is_valid():
                messages.success(request,'Registration Success!')
                fm.save()
                fm = SignUp()
        else:
            fm = SignUp()
        return render(request,'core/signup.html',{'forms':fm})
    else:
        return HttpResponseRedirect('/dashboard/')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data = request.POST)
            if fm.is_valid():
                unam = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=unam, password =upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm = AuthenticationForm()

        return render(request,'core/login.html',{'forms':fm})
    else:
        return HttpResponseRedirect('/dashboard/')


def profile(request):
    if request.user.is_authenticated:
        return render(request,'core/profile.html')
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
        



def changepassword(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user = request.user,data =request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Password Changed Success!')
            update_session_auth_hash(request,fm.user)
            return HttpResponseRedirect('/dashboard/')
    else:
        fm = PasswordChangeForm(user = request.user)
    return render(request,'core/changepassword.html',{'forms':fm})
