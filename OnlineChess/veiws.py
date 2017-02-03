from django.http import HttpResponse , HttpResponseRedirect
#from django.shortcuts import render_to_response
from django.template import Template , Context
from django.template.loader import get_template
from django.core.mail import send_mail
from chess.models import users
def index(request):
    if(request.method=='GET'):
        t = get_template('index.html')
        html = t.render(Context({}))
        return HttpResponse(html)
    else:
        tmp=0
        hell=[]
        for i in users.objects.all():
            hell.append(i.name)
        errors = []
        if(request.POST.get('un') in hell):
            user=users.objects.get(name=request.POST.get('un'))
            if(user.key!=request.POST.get('pw')):
                errors.append("wrong password")
            if(user.active==0):
                errors.append("your account has not activated yet :D")
        else:
            t = get_template('index.html')
            html = t.render(Context({'errors':"this username doesnt exist :D"}))
            return HttpResponse(html)
        if(errors):
            t = get_template('index.html')
            html = t.render(Context({'errors':errors}))
            return HttpResponse(html)
        else:
            pass
            #under building coming soon!!



        # return render_to_response("../templates/index.html")
def sign(request):
    if(request.method=='POST'):
        errors=[]
        actc=0
        if(not request.POST.get('sus','')):
            errors.append('UserName Is Necessary')
        if(not request.POST.get('spw','')):
            errors.append('password Is Necessary ')
        if(not request.POST.get('smail','') or '@' not in request.POST['smail']):
            errors.append('A Valid Email is Necessary')
        tmp=[]
        for i in users.objects.all():
            tmp.append(i.name)
        if(request.POST['sus'] in tmp):
            errors.append("Someone already has that username please try another one")
        if not errors:
            tmp=str(list(request.POST['sus']))
            for i in tmp:
                actc+=ord(i)
            actc=actc%10000
            actc=actc+2016
            print("<<<<<<<<<<<",actc)
            massage='this is your activation code \n' + str(actc)
            a=users(name=str(request.POST['sus']),key=str(request.POST['spw']),email=str(request.POST['smail']),active=False,wins=0,actcode=actc)
            #send_mail('Activation code',massage,'admin@OnlineChess.com',list(request.POST['smail']),fail_silently=False)
            a.save()
            request.session['user_name']=a.name
            request.method='GET'
            return HttpResponseRedirect('/activate')
        else:
            t = get_template('signup.html')
            html = t.render(Context({'errors':errors}))
            return HttpResponse(html)
    else:
        t = get_template('signup.html')
        html = t.render(Context({}))
        return HttpResponse(html)
def activate(request):
    if(request.session):
        if(request.method=='POST'):
            errors=''
            m = users.objects.get(name=request.session['user_name'])
            if(request.POST.get('scode')!=m.actcode):
                errors='wrong code'
            if(errors==''):
                m.active=1
                m.save()
                t=get_template('activate.html')
                html=t.render(Context({'result':'your account activated now try index page to login'}))
                return HttpResponse(html)
            else:
                t=get_template('activate.html')
                html=t.render(Context({'result':errors}))
                return HttpResponse(html)
        else:
            t = get_template('activate.html')
            html = t.render(Context({'result': ''}))
            return HttpResponse(html)
    else:
        return HttpResponse("An error ocurred because U try too conndect this page without sign up :D")



