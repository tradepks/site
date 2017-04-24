from django.conf.urls import url
from . import views
from django.conf.urls import include,url

urlpatterns = [	
	#  /qt/details/
	url(r'^details/(?P<symbols>[\w-]+)$',views.MyView.as_view(), name='quotes-details'),	
    #/qt/submit/
    url(r'^submit/$',views.submit_form, name='subit-form-submission'),
    #/qt/nasdaq/
    url(r'^nasdaq/$', views.GetTicker.as_view(),kwargs={'csv': 'NASDAQcompanylistU.csv'}, name='subit-form-submission'),
	
	]
