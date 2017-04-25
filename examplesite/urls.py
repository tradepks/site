from django.conf.urls import url
from django.contrib import admin
from .views import MyView
from . import views
from django.conf.urls import include as original_include 
from machina.app import board
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^admin/', admin.site.urls),       
    url(r'^register_activate/',original_include('register_activate.urls')),   
    url(r'^qt/', original_include('finance.urls')), 
    url(r'^environ/$', MyView.as_view()),    
    url(r'^$', views.index, name='main_index'),   
    
    #Machina
    url(r'^forum/', original_include(board.urls)),
]

#Machina 
from django.conf import settings 
if settings.DEBUG:
    # Add the Debug Toolbar’s URLs to the project’s URLconf
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', original_include(debug_toolbar.urls)), ]

    # In DEBUG mode, serve media files through Django.
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.views import static
    urlpatterns += staticfiles_urlpatterns()
    # Remove leading and trailing slashes so the regex matches.
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += [
        url(r'^%s/(?P<path>.*)$' % media_url, static.serve,
            {'document_root': settings.MEDIA_ROOT}),
    ]