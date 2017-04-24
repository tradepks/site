from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse,QueryDict
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from datetime import *
from .forms import SignupForm, SigninForm
from django.shortcuts import get_object_or_404




def sign_up(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user_instance=form.save()
			username=request.POST['username']
			password=request.POST['password']            
			user=authenticate(username=username,password=password)
			#The user is not active until they activate their account through email
			user.is_active=False
			user.save()
			id=user.id
			email=user.email
			quick_send_email(email,id)
			return render(request,'thankyou.html')
		else:
			return render(request,'sign_up.html',{'form':form})
	else:
		form = SignupForm()
		return render(request,'sign_up.html',{'form':form, 'help_text': ''})


def activate(request):
	id=int(request.GET.get('id'))
	user = User.objects.get(id=id)
	user.is_active=True
	user.save()
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
				if user.is_active:											#Make sure the account is activated
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
def quick_send_email(toaddr,id):
    message = "Hi!\nHow are you?\nHere is the link to activate your account:\nhttp://127.0.0.1:8000/register_activate/activation/?id=%s" %(id)   
    subject="Activate your account at Tradepks"
    
    #Use gmail's smtp server to send email. However, you need to turn on the setting "lesssecureapps" following this link:
    #https://www.google.com/settings/security/lesssecureapps
    send_mail(subject, message, settings.EMAIL_HOST_USER, [toaddr,] )
  
