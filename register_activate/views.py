from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse,QueryDict
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from datetime import *
from .forms import SignupForm, SigninForm
from django.shortcuts import get_object_or_404
from .models import Activation
import datetime
from django.core.urlresolvers import reverse
from  django.utils import timezone
from django.http import Http404

def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user_instance=form.save()
            username=request.POST['username']
            password=request.POST['password']   
            #checks them against each authentication backend, including ours
            #and returns a User object if the credentials are valid for a backend
            #Handle None 
            user=authenticate(username=username,password=password)
            #The user is not active until they activate their account through email
            user.is_active=False
            user.save()
            id=user.id
            #Create Activation record 
            act = Activation(user_id=id)
            act.save()            
            email=user.email
            quick_send_email(request, email,act)
            return render(request,'thankyou.html')
        else:
            return render(request,'sign_up.html',{'form':form})
    else:
        form = SignupForm()
        return render(request,'sign_up.html',{'form':form, 'help_text': ''})


def activate(request):
    id, salt = request.GET.get('id').split("-")
    user = get_object_or_404(User, id=int(id))
    act = get_object_or_404(Activation, user_id=int(id))
    expiry_date = act.activation_request_date + datetime.timedelta(days=1)
    if user.is_active == True or act.salt != salt or timezone.now() > expiry_date:
        raise Http404("Was already activated or id corrupted or expired, Take suitable Steps")
    user.is_active=True
    user.save()
    act.save() #update activated_on
    return render(request,'activation.html')


def sign_in(request):
    if request.method=='POST':
        form=SigninForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            next =request.POST.get('next', "/")
            user =authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:                                            #Make sure the account is activated
                    login(request,user)
                    return redirect(next)
        
                else:
                    return render(request,'ErrorPage.html')
            else:
                return render(request,'ErrorPage.html',{'errormessage':'Invalid login'})
        else:
            return render(request,'sign_in.html',{'form':form})
    else:
        form=SigninForm()
        next = request.GET.get("next", "/")
        return render(request,'sign_in.html',{'form':form, 'next': next})




def log_out(request):
    logout(request)
    return render(request,'log_out.html')

    
#Use Django sendmail 
from django.core.mail import send_mail
from django.conf import settings
def quick_send_email(request,toaddr,act):
    expiry_date = act.activation_request_date + datetime.timedelta(days=1)
    link = request.build_absolute_uri(reverse("register_activate:activation"))
    message = """
    Hi!

    How are you?

    Here is the link to activate your account by %s:
    %s?id=%s-%s""" % (expiry_date, link, act.user_id, act.salt)   

    subject="Activate your account at Tradepks"

    #Use gmail's smtp server to send email. However, you need to turn on the setting "lesssecureapps" following this link:
    #https://www.google.com/settings/security/lesssecureapps
    send_mail(subject, message, settings.EMAIL_HOST_USER, [toaddr,] )
  

  
  
  
  
def custom_404(request):
    return render(request, "404.html", {'message': " Take suitable Steps " })