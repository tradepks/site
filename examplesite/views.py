from django.views.generic.base import TemplateView
import os 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin



import logging
log = logging.getLogger(__name__)

#LoginRequiredMixin , any mixin should be first 
class MyView(LoginRequiredMixin, TemplateView):
    template_name = "environ.html"
    login_url = '/register_activate/signin/' 
    def get_context_data(self, **kwargs):
        context = super(MyView, self).get_context_data(**kwargs)
        context['objects'] = os.environ
        return context

 




@login_required(login_url='/register_activate/signin/')
def index(request):
	if request.method == 'GET':
		message="You are logged in successfully"
		return render(request,'mainpage.html',{'user':request.user,'message':message})
	elif request.method =='POST':
		if request.POST.get("logout"):
			return redirect('register_activate:logout')
		else:
			return redirect('register_activate:thankyou')
