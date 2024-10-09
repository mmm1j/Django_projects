from django.shortcuts import render, redirect
from django.http import HttpResponse
import html
from django.views.decorators.csrf import csrf_exempt
from django.views import View
# Call as dumpdata('GET', request.GET)
from django.middleware.csrf import get_token
from django.shortcuts import render

def cookies(request):
    response_str = """ <p>hello</p> """
    resp = HttpResponse(response_str)
    resp.set_cookie('author','Prots')
    num_visits = request.session.get('num_visits',0) +1
    resp.set_cookie('num_of_visits',num_visits)
    

   
    
    return resp

