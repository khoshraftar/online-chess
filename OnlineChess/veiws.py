from django.http import HttpResponse
#from django.shortcuts import render_to_response
from django.template import Template , Context
from django.template.loader import get_template
def index(request):
    t = get_template('index.html')
    html = t.render(Context({"ali":"sign up"}))
    return HttpResponse(html)
        # return render_to_response("../templates/index.html")
def sign(request):
    t = get_template('signup.html')
    html = t.render(Context({}))
    return HttpResponse(html)