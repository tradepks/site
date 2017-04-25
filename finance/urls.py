from django.conf.urls import url
from . import views
from django.conf.urls import include,url

urlpatterns = [	
	#  /qt/details/
	url(r'^details/(?P<symbols>[\w\-:]+)$',views.MyView.as_view(), name='quotes-details'),	
    #/qt/submit/
    url(r'^submit/$',views.submit_form, name='submit-form-submission'),
    #/qt/download/
    url(r'^download/$',views.download_ticker, name='download-ticker'),
    #/qt/nasdaq/
    url(r'^nasdaq/$', views.GetTicker.as_view(),kwargs={'csv': 'NASDAQ.csv', 'type': 'NASDAQ'}, name='subit-form-submission'),
	
	]
