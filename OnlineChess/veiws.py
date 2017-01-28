from django.http import HttpResponse
from django.template import Template , Context
def hello(request):
    return HttpResponse("Hello world")