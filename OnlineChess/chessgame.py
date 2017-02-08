from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.template.loader import get_template
from django.core.mail import send_mail
from chess.models import users
from OnlineChess.classes import pieces, chessboard
import json
from OnlineChess.moving import checkt
from django.contrib.staticfiles.templatetags.staticfiles import static
def game(request):
    if (request.session.get++('user_name', None) == None):
        return HttpResponse("you have not permission please sign in first :D")
    else:
        try:
            user = users.objects.get(name=request.session['user_name'])
        except:
            return HttpResponse("please sign in :D")
        if (request.method == "GET"):
            t = get_template('chessgame.html')
            html = t.render(Context({'user': user.name, 'value': 'start!'}))
            return HttpResponse(html)

        else:
            CG = chessboard()
            CG.turn = user.turn
            CG.a = json.loads(user.game)
            t = get_template('chessgame.html')
            tmp = {}
            for i in range(8):
                for j in range(8):
                    if (CG.a[i][j] != None):
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'brook'):
                            tmp["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/BlackRook.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bknight'):
                            tmp["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/BlackKnight.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bbishop'):
                            tmp["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/BlackBishop.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bking'):
                            tmp["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/BlackKing.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bqueen'):
                            tmp["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/BlackQueen.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bpawn'):
                            tmp["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/BlackPawn.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wrook'):
                            tmp["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/WhiteRook.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wknight'):
                            tmp["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/WhiteKnight.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wbishop'):
                            tmp["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/WhiteBishop.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wking'):
                            tmp["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/WhiteKing.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wqueen'):
                            tmp["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/WhiteQueen.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wpawn'):
                            tmp["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/WhitePawn.png') + '" alt="My image"/>')
            tmp['user']=request.session['user_name']
            html = t.render(Context(tmp))
            return HttpResponse(html)

def ongame(requset):
    if (requset.method == 'POST'):
        if(requset.POST['javad'][0]=='f'):
            user = users.objects.get(name=requset.session['user_name'])
            CG = chessboard()
            CG.turn = user.turn
            CG.a = json.loads(user.game)
            y1 = int(requset.POST['javad'][1])
            x1 = int(requset.POST['javad'][2])
            requset.session['x']=x1
            requset.session['y']=y1
            tmpp = pieces()
            tmpp.x = x1
            tmpp.y = y1
            tmpp.type = (CG.a[y1 - 1][x1 - 1])[1:len(CG.a[y1 - 1][x1 - 1]) - 1]
            tmpp.id = CG.a[y1 - 1][x1 - 1]
            tmpp.side = CG.a[y1 - 1][x1 - 1][0]
            if(tmpp.side=='b'):
                return HttpResponse("0")
            help = checkt(CG, tmpp)
            hello = {}
            for i in help[0]:
                hello["style%i%i"%(i[1],i[0])]="style='border: 3px lawngreen solid'"
            for i in help[1]:
                hello["style%i%i"%(i[1],i[0])]="style='border: 3px lawngreen solid'"
            for i in range(8):
                for j in range(8):
                    if (CG.a[i][j] != None):
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'brook'):
                            hello["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/BlackRook.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bknight'):
                            hello["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/BlackKnight.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bbishop'):
                            hello["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/BlackBishop.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bking'):
                            hello["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/BlackKing.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bqueen'):
                            hello["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/BlackQueen.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bpawn'):
                            hello["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/BlackPawn.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wrook'):
                            hello["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/WhiteRook.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wknight'):
                            hello["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/WhiteKnight.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wbishop'):
                            hello["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/WhiteBishop.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wking'):
                            hello["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/WhiteKing.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wqueen'):
                            hello["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/WhiteQueen.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wpawn'):
                            hello["a%i%i" % (i + 1,j + 1)] = ('<img src="' + static('chess/WhitePawn.png') + '" alt="My image"/>')
            t = get_template("chessgame.html")
            html = t.render(Context(hello))
            html2=""
            hkh=0
            for i in range(len(html)):
                if(str(html[i:i+28])=='<table style="margin: auto">'):
                    hkh=i+28
                    break
            for i in range(hkh,len(html)):
                if(html[i:i+8]=="</table>"):
                    break
                html2=html2+html[i]
            return HttpResponse(html2)
        if(requset.POST['javad'][0]=='m'):
            user = users.objects.get(name=requset.session['user_name'])
            CG = chessboard()
            CG.turn = user.turn
            CG.a = json.loads(user.game)
            y1 = int(requset.POST['javad'][1])
            x1 = int(requset.POST['javad'][2])
            user=users.objects.get(name=requset.session['user_name'])
            CG.a[y1-1][x1-1]
            #tmp.a[requset.session['y']][re]


