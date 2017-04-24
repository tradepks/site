from django.views.generic.base import TemplateView
import os 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
import json 
from googlefinance import getQuotes
from django.core.urlresolvers import reverse

#LoginRequiredMixin , any mixin should be first 
class MyView(TemplateView):
    template_name = "finance/quotes.html"    
    
    def get_context_data(self, **kwargs):
        context = super(MyView, self).get_context_data(**kwargs)
        symbols = kwargs.get('symbols', 'GOOG-AAPL')
        context['names'] = ['ID','StockSymbol','Index','LastTradePrice','LastTradeWithCurrency','LastTradeTime','LastTradeDateTime','LastTradeDateTimeLong','Dividend','Yield',]
        context['quotes'] = getQuotes(symbols.split("-"))
        return context

        
  
def submit_form(request):
    symbols = "-".join(request.POST.getlist('id[]'))    
    return redirect(reverse("quotes-details", kwargs={'symbols': symbols}))

        
   
class GetTicker(TemplateView):
    template_name = 'finance/viewer2.html'    
    
    def get_context_data(self, **kwargs):
        context = super(GetTicker, self).get_context_data(**kwargs)
        context['filename'] =  kwargs.get('csv', 'None')
        return context