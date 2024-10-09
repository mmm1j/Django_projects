# game/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
import html
from django.views.decorators.csrf import csrf_exempt
from django.views import View
# Call as dumpdata('GET', request.GET)
from django.middleware.csrf import get_token
from django.shortcuts import render

def dumpdata(place, data) :
    retval = ""
    if len(data) > 0 :
        retval += '<p>Incoming '+place+' data:<br/>\n'
        for key, value in data.items():
            retval += html.escape(key) + '=' + html.escape(value) + '</br>\n'
        retval += '</p>\n'
    return retval
#@csrf_exempt
def getform(request):
    response = """<p>Impossible POST guessing game...</p>
        <form method="post">
        <p><label for="guess">Input Guess</label>
        <input type="text" name="guess" size="40" id="guess"/></p>
        <input type="hidden" name="csrfmiddlewaretoken" 
            value="token"/>

        <input type="submit"/>
        </form>"""
    token = get_token(request)
    response= response.replace('__token__',html.escape(token))
    response += dumpdata('Post', request.POST)
    return HttpResponse(response)
class GuessGameViev(View):
    def get (self,request):
        return render (request,'guesgame/guess.html')
    def post(self,reqest):
        return HttpResponse("POST")