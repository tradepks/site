from django.conf.urls import url
from django.contrib import admin
from .views import MyView
from . import views
from django.conf.urls import include 


urlpatterns = [
    url(r'^admin/', admin.site.urls),       
    url(r'^register_activate/',include('register_activate.urls')),   
    url(r'^qt/',include('finance.urls')), 
    url(r'^environ/$', MyView.as_view()),    
    url(r'^$', views.index, name='main_index'),   
]
