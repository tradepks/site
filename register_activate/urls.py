from django.conf.urls import url
from . import views
from django.conf.urls import include,url
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
app_name='register_activate'
urlpatterns = [	
	# ex: /register_activate/signup/
	url(r'^signup/$',views.sign_up, name='signup'),
	# ex: /register_activate/activation/
	url(r'^activation/',views.activate, name='activation'),
	# ex: /register_activate/signin/
	url(r'^signin/$',views.sign_in, name='signin'),
	# ex: /register_activate/logout/
	url(r'^logout/$',views.log_out, name='logout'),

	]

handler404 = 'register_activate.views.custom_404'