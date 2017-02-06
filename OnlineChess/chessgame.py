from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.template.loader import get_template
from django.core.mail import send_mail
from chess.models import users
from OnlineChess.classes import pieces, chessboard
import json

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
            html = t.render(Context({'user': user.name, 'value': 'start!'}))
            return HttpResponse(html)

        else:
            CG=chessboard()
            CG.turn=user.turn
            CG.a=json.loads(user.game)
            t = get_template('chessgame.html')
            tmp={}
            for i in range(8):
                for j in range(8):
                    if(CG.a[i][j]!=None):
                        tmp["a%i%i"%(i+1,j+1)]=CG.a[i][j]
            html = t.render(Context(tmp))
            return HttpResponse(html)




def checkt(board, piece):
    ################################ rook #####################
    if (piece.type == 'rook'):
        moves = []
        attacks = []
        for i in range(piece.y + 1, 9):
            if (board.a[i - 1][piece.x - 1] != None):
                if (board.a[i - 1][piece.x - 1][0] == piece.side):
                    break
                if (board.a[i - 1][piece.x - 1][0] != piece.side):
                    attacks.append((piece.x, i))
                    break
            moves.append((piece.x, i))

        for i in range(piece.y - 1, 0, -1):
            if (board.a[i - 1][piece.x - 1] != None):
                if (board.a[i - 1][piece.x - 1][0] == piece.side):
                    break
                if (board.a[i - 1][piece.x - 1][0] != piece.side):
                    attacks.append((piece.x, i))
                    break
            moves.append((piece.x, i))

        for i in range(piece.x + 1, 9):
            if (board.a[piece.y - 1][i - 1] != None):
                if (board.a[piece.y - 1][i - 1][0] == piece.side):
                    break
                if (board.a[piece.y - 1][i - 1][0] != piece.side):
                    attacks.append((i, piece.y))
                    break
            moves.append((i, piece.y))

        for i in range(piece.x - 1, 0, -1):
            if (board.a[piece.y - 1][i - 1] != None):
                if (board.a[piece.y - 1][i - 1][0] == piece.side):
                    break
                if (board.a[piece.y - 1][i - 1][0] != piece.side):
                    attacks.append((i, piece.y))
                    break
            moves.append((i, piece.y))
    ############################## knight ##################
    if (piece.type == 'knight'):
        moves = []
        attacks = []
        ##
        xtmp = piece.x - 1
        ytmp = piece.y + 2
        if (ytmp <= 8 and xtmp >= 1):
            if (board.a[ytmp - 1][xtmp - 1] != None):
                if (board.a[ytmp - 1][xtmp - 1][0] != piece.side):
                    attacks.append((xtmp, ytmp))
            else:
                moves.append((xtmp, ytmp))
        ##
        xtmp = piece.x + 1
        ytmp = piece.y + 2
        if (ytmp <= 8 and xtmp <= 8):
            if (board.a[ytmp - 1][xtmp - 1] != None):
                if (board.a[ytmp - 1][xtmp - 1][0] != piece.side):
                    attacks.append((xtmp, ytmp))
            else:
                moves.append((xtmp, ytmp))

        ##
        xtmp = piece.x + 2
        ytmp = piece.y + 1
        if (ytmp <= 8 and xtmp <= 8):
            if (board.a[ytmp - 1][xtmp - 1] != None):
                if (board.a[ytmp - 1][xtmp - 1][0] != piece.side):
                    attacks.append((xtmp, ytmp))
            else:
                moves.append((xtmp, ytmp))
        ##
        xtmp = piece.x + 2
        ytmp = piece.y - 1
        if (ytmp >= 1 and xtmp <= 8):
            if (board.a[ytmp - 1][xtmp - 1] != None):
                if (board.a[ytmp - 1][xtmp - 1][0] != piece.side):
                    attacks.append((xtmp, ytmp))
            else:
                moves.append((xtmp, ytmp))
        ##
        xtmp = piece.x + 1
        ytmp = piece.y - 2
        if (ytmp >= 1 and xtmp <= 8):
            if (board.a[ytmp - 1][xtmp - 1] != None):
                if (board.a[ytmp - 1][xtmp - 1][0] != piece.side):
                    attacks.append((xtmp, ytmp))
            else:
                moves.append((xtmp, ytmp))
        ##
        xtmp = piece.x - 1
        ytmp = piece.y - 2
        if (ytmp >= 1 and xtmp >= 1):
            if (board.a[ytmp - 1][xtmp - 1] != None):
                if (board.a[ytmp - 1][xtmp - 1][0] != piece.side):
                    attacks.append((xtmp, ytmp))
            else:
                moves.append((xtmp, ytmp))
        ##
        xtmp = piece.x - 2
        ytmp = piece.y - 1
        if (ytmp >= 1 and xtmp <= 8):
            if (board.a[ytmp - 1][xtmp - 1] != None):
                if (board.a[ytmp - 1][xtmp - 1][0] != piece.side):
                    attacks.append((xtmp, ytmp))
            else:
                moves.append((xtmp, ytmp))
        ##
        xtmp = piece.x - 2
        ytmp = piece.y + 1
        if (ytmp <= 8 and xtmp >= 1):
            if (board.a[ytmp - 1][xtmp - 1] != None):
                if (board.a[ytmp - 1][xtmp - 1][0] != piece.side):
                    attacks.append((xtmp, ytmp))
            else:
                moves.append((xtmp, ytmp))
    ###################################### bishop ####################
    if (piece.type == 'bishop'):
        moves = []
        attacks = []
        ##
        itmp = piece.x + 1
        jtmp = piece.y + 1
        while (True):
            if (itmp > 8 or jtmp > 8):
                break
            if (board.a[jtmp - 1][itmp - 1] != None):
                if (board.a[jtmp - 1][itmp - 1][0] == piece.type):
                    break
                else:
                    attacks.append((itmp, jtmp))
                    break
            moves.append((itmp, jtmp))
            itmp += 1
            jtmp += 1
        ##
        itmp = piece.x - 1
        jtmp = piece.y + 1
        while (True):
            if (itmp < 1 or jtmp > 8):
                break
            if (board.a[jtmp - 1][itmp - 1] != None):
                if (board.a[jtmp - 1][itmp - 1][0] == piece.type):
                    break
                else:
                    attacks.append((itmp, jtmp))
                    break
            moves.append((itmp, jtmp))
            itmp -= 1
            jtmp += 1
        ##
        itmp = piece.x - 1
        jtmp = piece.y - 1
        while (True):
            if (itmp < 1 or jtmp < 1):
                break
            if (board.a[jtmp - 1][itmp - 1] != None):
                if (board.a[jtmp - 1][itmp - 1][0] == piece.type):
                    break
                else:
                    attacks.append((itmp, jtmp))
                    break
            moves.append((itmp, jtmp))
            itmp -= 1
            jtmp -= 1
        ##
        itmp = piece.x + 1
        jtmp = piece.y - 1
        while (True):
            if (itmp > 8 or jtmp < 1):
                break
            if (board.a[jtmp - 1][itmp - 1] != None):
                if (board.a[jtmp - 1][itmp - 1][0] == piece.type):
                    break
                else:
                    attacks.append((itmp, jtmp))
                    break
            moves.append((itmp, jtmp))
            itmp += 1
            jtmp -= 1
    if (piece.type == 'queen'):
        moves = []
        attacks = []
        ##
        itmp = piece.x + 1
        jtmp = piece.y + 1
        while (True):
            if (itmp > 8 or jtmp > 8):
                break
            if (board.a[jtmp - 1][itmp - 1] != None):
                if (board.a[jtmp - 1][itmp - 1][0] == piece.type):
                    break
                else:
                    attacks.append((itmp, jtmp))
                    break
            moves.append((itmp, jtmp))
            itmp += 1
            jtmp += 1
        ##
        itmp = piece.x - 1
        jtmp = piece.y + 1
        while (True):
            if (itmp < 1 or jtmp > 8):
                break
            if (board.a[jtmp - 1][itmp - 1] != None):
                if (board.a[jtmp - 1][itmp - 1][0] == piece.type):
                    break
                else:
                    attacks.append((itmp, jtmp))
                    break
            moves.append((itmp, jtmp))
            itmp -= 1
            jtmp += 1
        ##
        itmp = piece.x - 1
        jtmp = piece.y - 1
        while (True):
            if (itmp < 1 or jtmp < 1):
                break
            if (board.a[jtmp - 1][itmp - 1] != None):
                if (board.a[jtmp - 1][itmp - 1][0] == piece.type):
                    break
                else:
                    attacks.append((itmp, jtmp))
                    break
            moves.append((itmp, jtmp))
            itmp -= 1
            jtmp -= 1
        ##
        itmp = piece.x + 1
        jtmp = piece.y - 1
        while (True):
            if (itmp > 8 or jtmp < 1):
                break
            if (board.a[jtmp - 1][itmp - 1] != None):
                if (board.a[jtmp - 1][itmp - 1][0] == piece.type):
                    break
                else:
                    attacks.append((itmp, jtmp))
                    break
            moves.append((itmp, jtmp))
            itmp += 1
            jtmp -= 1
        #########
        for i in range(piece.y + 1, 9):
            if (board.a[i - 1][piece.x - 1] != None):
                if (board.a[i - 1][piece.x - 1][0] == piece.side):
                    break
                if (board.a[i - 1][piece.x - 1][0] != piece.side):
                    attacks.append((piece.x, i))
                    break
            moves.append((piece.x, i))

        for i in range(piece.y - 1, 0, -1):
            if (board.a[i - 1][piece.x - 1] != None):
                if (board.a[i - 1][piece.x - 1][0] == piece.side):
                    break
                if (board.a[i - 1][piece.x - 1][0] != piece.side):
                    attacks.append((piece.x, i))
                    break
            moves.append((piece.x, i))

        for i in range(piece.x + 1, 9):
            if (board.a[piece.y - 1][i - 1] != None):
                if (board.a[piece.y - 1][i - 1][0] == piece.side):
                    break
                if (board.a[piece.y - 1][i - 1][0] != piece.side):
                    attacks.append((i, piece.y))
                    break
            moves.append((i, piece.y))

        for i in range(piece.x - 1, 0, -1):
            if (board.a[piece.y - 1][i - 1] != None):
                if (board.a[piece.y - 1][i - 1][0] == piece.side):
                    break
                if (board.a[piece.y - 1][i - 1][0] != piece.side):
                    attacks.append((i, piece.y))
                    break
            moves.append((i, piece.y))
    if (piece.type == 'king'):
        attacks = []
        moves = []
        itmp = piece.x + 1
        jtmp = piece.y + 1
        if (itmp <= 8 and jtmp <= 8):
            if (board.a[jtmp - 1][itmp - 1] == None):
                moves.append((itmp, jtmp))
            else:
                if (board.a[jtmp - 1][itmp - 1][0] != piece.type):
                    attacks.append((itmp, jtmp))
        itmp = piece.x
        jtmp = piece.y + 1
        if (itmp <= 8 and jtmp <= 8):
            if (board.a[jtmp - 1][itmp - 1] == None):
                moves.append((itmp, jtmp))
            else:
                if (board.a[jtmp - 1][itmp - 1][0] != piece.type):
                    attacks.append((itmp, jtmp))
        itmp = piece.x - 1
        jtmp = piece.y + 1
        if (itmp >= 1 and jtmp <= 8):
            if (board.a[jtmp - 1][itmp - 1] == None):
                moves.append((itmp, jtmp))
            else:
                if (board.a[jtmp - 1][itmp - 1][0] != piece.type):
                    attacks.append((itmp, jtmp))
        itmp = piece.x - 1
        jtmp = piece.y
        if (itmp >= 1 and jtmp >= 1):
            if (board.a[jtmp - 1][itmp - 1] == None):
                moves.append((itmp, jtmp))
            else:
                if (board.a[jtmp - 1][itmp - 1][0] != piece.type):
                    attacks.append((itmp, jtmp))
        itmp = piece.x - 1
        jtmp = piece.y - 1
        if (itmp >= 1 and jtmp >= 1):
            if (board.a[jtmp - 1][itmp - 1] == None):
                moves.append((itmp, jtmp))
            else:
                if (board.a[jtmp - 1][itmp - 1][0] != piece.type):
                    attacks.append((itmp, jtmp))
        itmp = piece.x
        jtmp = piece.y - 1
        if (itmp <= 8 and jtmp >= 1):
            if (board.a[jtmp - 1][itmp - 1] == None):
                moves.append((itmp, jtmp))
            else:
                if (board.a[jtmp - 1][itmp - 1][0] != piece.type):
                    attacks.append((itmp, jtmp))
        itmp = piece.x + 1
        jtmp = piece.y - 1
        if (itmp <= 8 and jtmp >= 1):
            if (board.a[jtmp - 1][itmp - 1] == None):
                moves.append((itmp, jtmp))
            else:
                if (board.a[jtmp - 1][itmp - 1][0] != piece.type):
                    attacks.append((itmp, jtmp))
        itmp = piece.x + 1
        jtmp = piece.y
        if (itmp <= 8 and jtmp <= 8):
            if (board.a[jtmp - 1][itmp - 1] == None):
                moves.append((itmp, jtmp))
            else:
                if (board.a[jtmp - 1][itmp - 1][0] != piece.type):
                    attacks.append((itmp, jtmp))
    ################### pawn ########################

    if (piece.type == 'pawn'):
        attacks = []
        moves = []
        if (piece.side == 'w'):
            if (piece.y == 7):
                moves.append((piece.x, piece.y - 1))
                moves.append((piece.x, piece.y - 2))
            else:
                moves.append((piece.x, piece.y - 1))
            if (board.a[piece.y - 2][piece.x] != None and board[piece.y - 2][piece.x][0] != piece.side):
                attacks.append((piece.y - 1, piece.x + 1))
            if (board.a[piece.y - 2][piece.x - 2] != None and board[piece.y - 2][piece.x - 2][0] != piece.side):
                attacks.append((piece.y - 1, piece.x - 1))
        if (piece.side == 'b'):
            if (piece.y == 2):
                moves.append((piece.x, piece.y + 1))
                moves.append((piece.x, piece.y + 2))
            else:
                moves.append((piece.x, piece.y + 1))
            if (board.a[piece.y + 2][piece.x] != None and board[piece.y + 2][piece.x][0] != piece.side):
                attacks.append((piece.y - 1, piece.x + 1))
            if (board.a[piece.y + 2][piece.x - 2] != None and board[piece.y + 2][piece.x - 2][0] != piece.side):
                attacks.append((piece.y + 1, piece.x - 1))
    return (moves, attacks)

def ongame(requset):
    if (requset.method == 'POST'):
            return HttpResponse("hello world")