from django.shortcuts import render
from .forms import SignUp
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
import uuid
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def home(request):
    return render(request,'core/home.html')

def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignUp(request.POST)
            if fm.is_valid():
                
                new_user = fm.save()
                u_id = str(uuid.uuid4())
                pro_obj = Profile(user = new_user,token = u_id)
                pro_obj.save()
                sendemail(new_user.email, u_id)
                messages.success(request,'Registration Success, Verification link send in your email. Please Verify Your account!')
                fm = SignUp()
        else:
            fm = SignUp()
        return render(request,'core/signup.html',{'forms':fm})
    else:
        return HttpResponseRedirect('/dashboard/')

def sendemail(email,token):
    subject = 'Verify Email'
    message = f'Click on the link to verify your Account - http://127.0.0.1:8000/account-verify/{token}'
    print(message)
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)


def account_verify(request,token):
    pf = Profile.objects.filter(token = token).first()
    pf.verify = True
    pf.save()
    messages.success(request,'Your Account is verifed!')
    return HttpResponseRedirect('/signup')
    


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
