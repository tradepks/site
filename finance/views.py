from django.views.generic.base import TemplateView
import os 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
import json, os.path
from googlefinance import getQuotes
from django.core.urlresolvers import reverse
import requests
from django.http import HttpResponse
from django.conf import settings 



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


def download_ticker(request):
    lines =[]
    def flatten(array):
        res = []
        for ele in array:
            if type(ele) is list:
                res += flatten(ele)
            else:
                res.append(ele)
        return res
    def update_last(item):
        #"http://www.nasdaq.com/symbol/pih"
        #"<a href='http://www.nasdaq.com/symbol/pih'>show</a>"
        item1 = item.strip('"')
        return "\"<a href='" + item1 + "'>" + item1 + "</a>\""
    def process(line):
        s_arr = [s.strip() for s in line.split(",")]
        tmp_arr = [ s_arr[0], s_arr[0:-2], update_last(s_arr[-2])] #last item is , so empty string   
        return ",".join( flatten(tmp_arr)) + ",\n"  
        
    for url,path in settings.URLS_LIST_FOR_DOWNLOAD.items():
        content = requests.get(url).content
        with open(os.path.join(settings.COMPANY_LIST_DIR[0],path),'wb') as f:
            f.write(content)
        with open(os.path.join(settings.COMPANY_LIST_DIR[0],path)) as f:
            lines = f.readlines()
        #process, Copy first column, format last column 
        u_lines = [process(line) for line in lines]
        with open(os.path.join(settings.COMPANY_LIST_DIR[0],path), "w") as f:
           f.writelines(u_lines)
    return HttpResponse("Download succeed")
    
   
class GetTicker(TemplateView):
    template_name = 'finance/viewer2.html'    
    
    def get_context_data(self, **kwargs):
        context = super(GetTicker, self).get_context_data(**kwargs)
        context['filename'] =  kwargs.get('csv', 'None')
        context['type'] =  kwargs.get('type', 'NYSE')
        return context