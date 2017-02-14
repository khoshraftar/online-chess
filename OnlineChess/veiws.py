from django.http import HttpResponse , HttpResponseRedirect
from django.template import Template , Context
from django.template.loader import get_template
from django.core.mail import send_mail
from chess.models import users
from random import randint
from OnlineChess.classes import chessboard
import json
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
            request.session['user_name']=user.name
            return HttpResponseRedirect("/game")



        # return render_to_response("../templates/index.html")
def sign(request):
    if(request.method=='POST'):
        errors=[]
        actc=0
        if(len(request.POST.get('sus','f'))<4):
            errors.append('A minimum 4 length UserName Is Necessary')
        if(len(request.POST.get('spw','f'))<4):
            errors.append('A minimum 4 length password Is Necessary ')
        if(not request.POST.get('smail','') or '@' not in request.POST['smail'] or '.' not in request.POST['smail']):
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
            actc=actc+randint(2016,6000)
            print("<<<<<< this is just for test >>>>>>",actc)
            massage='this is your activation code \n' + str(actc)
            addmail=request.POST['smail']
            tmp1=[]
            tmp1.append(addmail)
            a=users(name=str(request.POST['sus']),key=str(request.POST['spw']),email=str(request.POST['smail']),active=False,wins=0,actcode=actc)
            #send_mail('Activation code',massage,'admin@OnlineChess.com', tmp1,fail_silently=False)
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
    if(request.session.get('user_name',False)):
        if(request.method=='POST'):
            errors=''
            m = users.objects.get(name=request.session['user_name'])
            if(request.POST.get('scode')!=m.actcode):
                errors='wrong code'
            if(errors==''):
                m.active=1
                m.turn='w'
                tmp=chessboard()
                s=json.dumps(tmp.a)
                m.game=s
                m.turn=tmp.turn
                m.save()
                t=get_template('activated.html')
                html=t.render(Context({}))
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
def ranklist(requset):
    tmp=""
    counter=1
    for i in users.objects.all().reverse():
        tmp=tmp+'<tr><td>%i - %s</td><td>%i wins</td>'%(counter,i.name,i.wins)
        counter=counter+1
    t=get_template("rank.html")
    html=t.render(Context({"Hossein":tmp}))
    return HttpResponse(html)