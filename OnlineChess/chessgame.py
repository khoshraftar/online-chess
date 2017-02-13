from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.template.loader import get_template
from chess.models import users
from OnlineChess.classes import pieces, chessboard
import json
import copy
from OnlineChess.moving import checkt
from OnlineChess.gamecondition import *
from django.contrib.staticfiles.templatetags.staticfiles import static
from OnlineChess.AI import point , nextstep
def game(request):
    if (request.session.get('user_name', None) == None):
        return HttpResponse("you have not permission please sign in first :D")
    else:
        try:
            user = users.objects.get(name=request.session['user_name'])
        except:
            return HttpResponse("please sign in :D")
        if (request.method == "GET"):
            t = get_template('chessgame.html')
            html = t.render(Context({'user': user.name, 'type': 'submit'}))
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
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/BlackRook.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bknight'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/BlackKnight.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bbishop'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/BlackBishop.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bking'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/BlackKing.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bqueen'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/BlackQueen.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bpawn'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/BlackPawn.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wrook'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/WhiteRook.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wknight'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/WhiteKnight.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wbishop'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/WhiteBishop.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wking'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/WhiteKing.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wqueen'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/WhiteQueen.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wpawn'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/WhitePawn.png') + '" alt="My image"/>')
            tmp['user'] = request.session['user_name']
            tmp['type'] = 'hidden'
            html = t.render(Context(tmp))
            return HttpResponse(html)

def ongame(requset):
    if (requset.method == 'POST'):
        if (requset.POST['javad'][0] == 'f'):
            user = users.objects.get(name=requset.session['user_name'])
            CG = chessboard()
            CG.turn = user.turn
            CG.a = json.loads(user.game)
            y1 = int(requset.POST['javad'][1])
            x1 = int(requset.POST['javad'][2])
            requset.session['x'] = x1
            requset.session['y'] = y1
            tmpp = pieces()
            tmpp.x = x1
            tmpp.y = y1
            tmpp.type = (CG.a[y1 - 1][x1 - 1])[1:len(CG.a[y1 - 1][x1 - 1]) - 1]
            tmpp.id = CG.a[y1 - 1][x1 - 1]
            tmpp.side = CG.a[y1 - 1][x1 - 1][0]
            if (tmpp.side == 'b'):
                return HttpResponse("0")
            help = checkt(CG, tmpp,user.canrook)
            hello = {}
            trash = []
            for i in range(len(help[0])):
                jk = chessboard()
                jk.a = copy.deepcopy(CG.a)
                jk.a[help[0][i][1] - 1][help[0][i][0] - 1] = jk.a[y1 - 1][x1 - 1]
                jk.a[y1 - 1][x1 - 1] = None
                if (wmatecond(jk) == 'w'):
                    trash.append(i)
            for i in trash:
                help[0][i]=(0,0)
            trash = []
            for i in range(len(help[1])):
                jk = chessboard()
                jk.a = copy.deepcopy(CG.a)
                jk.a[help[1][i][1] - 1][help[1][i][0] - 1] = jk.a[y1 - 1][x1 - 1]
                jk.a[y1 - 1][x1 - 1] = None
                if (wmatecond(jk) == 'w'):
                    trash.append(i)
            for i in trash:
                help[1][i]=(0,0)
            for i in help[0]:
                if(i[0]):
                    hello["style%i%i" % (i[1], i[0])] = "style='border: 3px lawngreen solid'"
            for i in help[1]:
                if(i[0]):
                    hello["style%i%i" % (i[1], i[0])] = "style='border: 3px green solid'"
            if (wmatecond(CG)):
                for i in range(8):
                    for j in range(8):
                        if (CG.a[i][j] == 'wking1'):
                            hello["style%i%i" % (i+1,j+1)] = "style='border: 3px red solid'"
            if(bmatecond(CG)):
                for i in range(8):
                    for j in range(8):
                        if(CG.a[i][j]=='bking1'):
                            hello["style%i%i" % (i+1,j+1)]="style='border: 3px red solid'"
            for i in range(8):
                for j in range(8):
                    if (CG.a[i][j] != None):
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'brook'):
                            hello["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/BlackRook.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bknight'):
                            hello["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/BlackKnight.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bbishop'):
                            hello["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/BlackBishop.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bking'):
                            hello["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/BlackKing.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bqueen'):
                            hello["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/BlackQueen.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bpawn'):
                            hello["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/BlackPawn.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wrook'):
                            hello["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/WhiteRook.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wknight'):
                            hello["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/WhiteKnight.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wbishop'):
                            hello["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/WhiteBishop.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wking'):
                            hello["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/WhiteKing.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wqueen'):
                            hello["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/WhiteQueen.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wpawn'):
                            hello["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/WhitePawn.png') + '" alt="My image"/>')
            t = get_template("chessgame.html")
            hello['type'] = 'hidden'
            html = t.render(Context(hello))
            html2 = ""
            hkh = 0
            for i in range(len(html)):
                if (str(html[i:i + 28]) == '<table style="margin: auto">'):
                    hkh = i + 28
                    break
            for i in range(hkh, len(html)):
                if (html[i:i + 8] == "</table>"):
                    break
                html2 = html2 + html[i]
            return HttpResponse(html2)
        if (requset.POST['javad'][0] == 'm'):
            user = users.objects.get(name=requset.session['user_name'])
            CG = chessboard()
            CG.turn = user.turn
            CG.a = json.loads(user.game)
            y1 = int(requset.POST['javad'][1])
            x1 = int(requset.POST['javad'][2])
            user = users.objects.get(name=requset.session['user_name'])
            CG.a[y1 - 1][x1 - 1] = CG.a[requset.session['y'] - 1][requset.session['x'] - 1]
            CG.a[requset.session['y'] - 1][requset.session['x'] - 1] = None
            if(CG.a[y1-1][x1-1]=='wking1'):
                user.canrook=0
                user.save()
            if(checkmatecond(CG)=='b'):
                user.wins=user.wins+1
                hl=chessboard()
                user.game=json.dumps(hl.a)
                user.save()
                return HttpResponse("your opponent loosed <br/> if U want to paly again press F5")
            ############## important point <<<<<<<
            bmove=nextstep(CG)
            if(checkmatecond(CG)=='a'):
                hl=chessboard()
                user.game=json.dumps(hl.a)
                user.save()
                return HttpResponse("you loosed :D <br/> if U want to play again press F5")
            CG.a[bmove[1][1]-1][bmove[1][0]-1]=CG.a[bmove[0][1]-1][bmove[0][0]-1]
            CG.a[bmove[0][1]-1][bmove[0][0]-1]=None
            if(CG.a[bmove[1][1]-1][bmove[1][0]-1]=='bking1'):
                user.opcanrook=0
                user.save()
            ff = json.dumps(CG.a)
            user.game = ff
            user.save()
            t = get_template('chessgame.html')
            tmp = {}
            if (wmatecond(CG)):
                user.canrook=0
                k=0
                user.save()
                for i in range(8):
                    for j in range(8):
                        if (CG.a[i][j] == 'wking1'):
                            tmp["style%i%i" % (i+1,j+1)] = "style='border: 3px red solid'"
            if(bmatecond(CG)):
                user.opcanrook=0
                for i in range(8):
                    for j in range(8):
                        if(CG.a[i][j]=='bking1'):
                            tmp["style%i%i" % (i+1,j+1)]="style='border: 3px red solid'"
            for i in range(8):
                for j in range(8):
                    if (CG.a[i][j] != None):
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'brook'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/BlackRook.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bknight'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/BlackKnight.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bbishop'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/BlackBishop.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bking'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/BlackKing.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bqueen'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/BlackQueen.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bpawn'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/BlackPawn.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wrook'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/WhiteRook.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wknight'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/WhiteKnight.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wbishop'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/WhiteBishop.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wking'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/WhiteKing.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wqueen'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/WhiteQueen.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wpawn'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                            '<img src="' + static('chess/WhitePawn.png') + '" alt="My image"/>')
            tmp['user'] = requset.session['user_name']
            tmp['type'] = 'hidden'
            html = t.render(Context(tmp))
            html2 = ""
            hkh = 0
            for i in range(len(html)):
                if (str(html[i:i + 28]) == '<table style="margin: auto">'):
                    hkh = i + 28
                    break
            for i in range(hkh, len(html)):
                if (html[i:i + 8] == "</table>"):
                    break
                html2 = html2 + html[i]
            return HttpResponse(html2)
        if (requset.POST['javad'][0] == 'a'):
            user = users.objects.get(name=requset.session['user_name'])
            CG = chessboard()
            CG.turn = user.turn
            CG.a = json.loads(user.game)
            y1 = int(requset.POST['javad'][1])
            x1 = int(requset.POST['javad'][2])
            user = users.objects.get(name=requset.session['user_name'])
            CG.a[y1 - 1][x1 - 1] = CG.a[requset.session['y'] - 1][requset.session['x'] - 1]
            CG.a[requset.session['y'] - 1][requset.session['x'] - 1] = None
            if(checkmatecond(CG)=='b'):
                user.wins=user.wins+1
                hl=chessboard()
                user.game=json.dumps(hl.a)
                user.save()
                return HttpResponse("your opponent loosed:D <br/> if U want to play again press F5")
            bmove=nextstep(CG)
            if(checkmatecond(CG)=='a'):
                hl=chessboard()
                user.game=json.dumps(hl.a)
                user.save()
                return HttpResponse("you loosed :D <br/> if U want to play again press F5")
            CG.a[bmove[1][1]-1][bmove[1][0]-1]=CG.a[bmove[0][1]-1][bmove[0][0]-1]
            CG.a[bmove[0][1]-1][bmove[0][0]-1]=None
            ff = json.dumps(CG.a)
            user.game = ff
            user.save()
            t = get_template('chessgame.html')
            tmp = {}
            if (wmatecond(CG)):
                user.canrook=0
                user.save()
                for i in range(8):
                    for j in range(8):
                        if (CG.a[i][j] == 'wking1'):
                            tmp["style%i%i" % (j+1,i+1)] = "style='border: 3px red solid'"
            if(bmatecond(CG)):
                user.opcanrook=0
                user.save()
                for i in range(8):
                    for j in range(8):
                        if(CG.a[i][j]=='bking1'):
                            tmp["style%i%i" % (j+1,i+1)]="style='border: 3px red solid'"
            for i in range(8):
                for j in range(8):
                    if (CG.a[i][j] != None):
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'brook'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                                '<img src="' + static('chess/BlackRook.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bknight'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                                '<img src="' + static('chess/BlackKnight.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bbishop'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                                '<img src="' + static('chess/BlackBishop.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bking'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                                '<img src="' + static('chess/BlackKing.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bqueen'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                                '<img src="' + static('chess/BlackQueen.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'bpawn'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                                '<img src="' + static('chess/BlackPawn.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wrook'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                                '<img src="' + static('chess/WhiteRook.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wknight'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                                '<img src="' + static('chess/WhiteKnight.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wbishop'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                                '<img src="' + static('chess/WhiteBishop.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wking'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                                '<img src="' + static('chess/WhiteKing.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wqueen'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                                '<img src="' + static('chess/WhiteQueen.png') + '" alt="My image"/>')
                        if ((CG.a[i][j])[0:len(CG.a[i][j]) - 1] == 'wpawn'):
                            tmp["a%i%i" % (i + 1, j + 1)] = (
                                '<img src="' + static('chess/WhitePawn.png') + '" alt="My image"/>')
            tmp['user'] = requset.session['user_name']
            tmp['type'] = 'hidden'
            html = t.render(Context(tmp))
            html2 = ""
            hkh = 0
            for i in range(len(html)):
                if (str(html[i:i + 28]) == '<table style="margin: auto">'):
                    hkh = i + 28
                    break
            for i in range(hkh, len(html)):
                if (html[i:i + 8] == "</table>"):
                    break
                html2 = html2 + html[i]
            return HttpResponse(html2)
