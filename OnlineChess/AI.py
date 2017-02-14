from OnlineChess.classes import chessboard, pieces
from OnlineChess.moving import checkt
from OnlineChess.gamecondition import *
import copy


def bsteps(board):
    moves = []
    attacks = []
    for i in [7,6,5,4,3,2,1,0]:
        for j in [4,3,5,2,6,1,7,0]:
            if (board.a[i][j] != None and board.a[i][j][0] == 'b'):
                p = pieces()
                p.x = j + 1
                p.y = i + 1
                p.type = board.a[i][j][1:len(board.a[i][j]) - 1]
                p.id = board.a[i][j]
                p.side = 'b'
                if (len(checkt(board, p, 0)[1])):
                    moveha = checkt(board, p, 0)[1]
                    for k in moveha:
                        btmp = chessboard()
                        btmp.a = copy.deepcopy(board.a)
                        btmp.a[k[1] - 1][k[0] - 1] = btmp.a[i][j]
                        btmp.a[i][j] = None
                        if (bmatecond(btmp) == 0):
                            attacks.append(((j + 1, i + 1), k))
                if (len(checkt(board, p, 0)[0])):
                    moveha = checkt(board, p, 0)[0]
                    for k in moveha:
                        btmp = chessboard()
                        btmp.a = copy.deepcopy(board.a)
                        btmp.a[k[1] - 1][k[0] - 1] = btmp.a[i][j]
                        btmp.a[i][j] = None
                        if (bmatecond(btmp) == 0):
                            moves.append(((j + 1, i + 1), k))
    allsteps = moves + attacks
    return allsteps


def wsteps(board):
    moves = []
    attacks = []
    for i in [7,6,5,4,3,2,1]:
        for j in [4,3,5,2,6,1,7,0]:
            if (board.a[i][j] != None and board.a[i][j][0] == 'w'):
                p = pieces()
                p.x = j + 1
                p.y = i + 1
                p.type = board.a[i][j][1:len(board.a[i][j]) - 1]
                p.id = board.a[i][j]
                p.side = 'w'
                if (len(checkt(board, p, 0)[1])):
                    moveha = checkt(board, p, 0)[1]
                    for k in moveha:
                        btmp = chessboard()
                        btmp.a = copy.deepcopy(board.a)
                        btmp.a[k[1] - 1][k[0] - 1] = btmp.a[i][j]
                        btmp.a[i][j] = None
                        if (bmatecond(btmp) == 0):
                            attacks.append(((j + 1, i + 1), k))
                if (len(checkt(board, p, 0)[0])):
                    moveha = checkt(board, p, 0)[0]
                    for k in moveha:
                        btmp = chessboard()
                        btmp.a = copy.deepcopy(board.a)
                        btmp.a[k[1] - 1][k[0] - 1] = btmp.a[i][j]
                        btmp.a[i][j] = None
                        if (bmatecond(btmp) == 0):
                            moves.append(((j + 1, i + 1), k))
    allsteps = moves + attacks
    return allsteps


def point(board):
    a = 0
    if (checkmatecond(board) == 'b'):
        return (-1)*(10 ** 4)
    if (checkmatecond(board) == 'w'):
        return (10 ** 4)
    for i in range(8):
        for j in range(8):
            if (board.a[i][j] != None):
                if (board.a[i][j][0:-1] == 'brook'):
                    a = a + 5
                if (board.a[i][j][0:-1] == 'bknight'):
                    a = a + 3
                if (board.a[i][j][0:-1] == 'bbishop'):
                    a = a + 3
                if (board.a[i][j][0:-1] == 'bqueen'):
                    a = a + 9
                if (board.a[i][j][0:-1] == 'bpawn'):
                    a = a + 1
                if (board.a[i][j][0:-1] == 'wrook'):
                    a = a - 5
                if (board.a[i][j][0:-1] == 'wknight'):
                    a = a - 3
                if (board.a[i][j][0:-1] == 'wbishop'):
                    a = a - 3
                if (board.a[i][j][0:-1] == 'wqueen'):
                    a = a - 9
                if (board.a[i][j][0:-1] == 'wpawn'):
                    a = a -  1
    if(wmatecond(board)=='w'):
        a=a+1
    if(bmatecond(board)=='b'):
        a=a-1
    return a

### s harekat check mikone
def AI(board, depth,mdepth):
    if (depth >= mdepth):
        return [point(board), (-1, -1)]
    if (depth % 2 == 0):
        mx = [(-1) * (10 ** 5), (-1, -1)]
        for i in bsteps(board):
            boardtmp = chessboard()
            boardtmp.a = copy.deepcopy(board.a)
            boardtmp.a[i[1][1] - 1][i[1][0] - 1] = boardtmp.a[i[0][1] - 1][i[0][0] - 1]
            boardtmp.a[i[0][1] - 1][i[0][0] - 1] = None
            tmp = AI(boardtmp, depth + 1,mdepth)
            if (tmp[0] > mx[0]):
                mx[0] = tmp[0]
                mx[1] = i
        return mx
    else:
        mn = [(10 ** 5), (-1, -1)]
        for i in wsteps(board):
            boardtmp = chessboard()
            boardtmp.a = copy.deepcopy(board.a)
            boardtmp.a[i[1][1] - 1][i[1][0] - 1] = boardtmp.a[i[0][1] - 1][i[0][0] - 1]
            boardtmp.a[i[0][1] - 1][i[0][0] - 1] = None
            tmp = AI(boardtmp, depth + 1,mdepth)
            if (tmp[0] < mn[0]):
                mn[0] = tmp[0]
                mn[1] = i
        return mn


def nextstep(board):
    count=0
    for i in range(8):
        for j in range(8):
            if(board.a[i][j]!=None):
                count=count+1
    if(count>6):
        return AI(board, 0,2)[1]
    if(count>4):
        return AI(board,0,4)[1]
    return AI(board,0,6)
