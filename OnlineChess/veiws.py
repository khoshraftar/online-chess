from django.http import HttpResponse
#from django.shortcuts import render_to_response
from django.template import Template , Context
from django.template.loader import get_template
from django.template import Context
def hello(request):
    t = get_template('index.html')
    html = t.render(Context({"ali":"sign up"}))
    return HttpResponse(html)
        # return render_to_response("../templates/index.html")