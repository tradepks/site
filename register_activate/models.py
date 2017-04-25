from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from .forms import make_salt

from django.contrib.auth.models import User

##Remember to use this command to create the tables you need in your database
##python manage.py migrate


class Activation(models.Model):                   #two field  
    user_id = models.IntegerField()
    salt = models.CharField(max_length=10, default=make_salt)
    activation_request_date = models.DateTimeField(auto_now_add=True)  #record creation date 
    activated_on = models.DateTimeField(auto_now=True)                 #record updated date

    def __str__(self):              # __str__ on Python 3, __unicode__ in Python2
        return self.name

    
    

