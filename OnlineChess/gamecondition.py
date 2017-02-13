from OnlineChess.moving import checkt
from OnlineChess.classes import pieces, chessboard
import copy
def bmatecond(board):
    ################# black ################
    bking=(0,0)
    for i in range(8):
        tmp=0
        for j in range(8):
            if(board.a[i][j]=='bking1'):
                bking=(j+1,i+1)
                tmp=1
                break
        if(tmp):
            break
    for i in range(8):
        for j in range(8):
            if(board.a[i][j]!=None and board.a[i][j][0]=='w'):
                p=pieces()
                p.type=board.a[i][j][1:len(board.a[i][j])-1]
                p.id=board.a[i][j]
                p.side='w'
                p.x=j+1
                p.y=i+1
                if(bking in checkt(board,p,0)[1]):
                    return 'b'
    return 0
def wmatecond(board):
    #################### white ######################
    wking = (0, 0)
    for i in range(8):
        tmp = 0
        for j in range(8):
            if (board.a[i][j] == 'wking1'):
                wking = (j + 1, i + 1)
                tmp = 1
                break
        if (tmp):
            break
    for i in range(8):
        for j in range(8):
            if (board.a[i][j] != None and board.a[i][j][0] == 'b'):
                p = pieces()
                p.type = board.a[i][j][1:len(board.a[i][j]) - 1]
                p.id = board.a[i][j]
                p.side = 'b'
                p.x = j + 1
                p.y = i + 1
                if (wking in checkt(board, p,0)[1]):
                    return 'w'
    return 0
def checkmatecond(board):
    ################## black #################
    if(bmatecond(board)=='b'):
        for i in range(8):
            for j in range(8):
                if(board.a[i][j]!=None and board.a[i][j][0]=='b'):
                    ptmp=pieces()
                    ptmp.type=board.a[i][j][1:len(board.a[i][j])-1]
                    ptmp.id=board.a[i][j]
                    ptmp.side='b'
                    ptmp.x=j+1
                    ptmp.y=i+1
                    for k in checkt(board,ptmp,0)[0]:
                        btmp=chessboard()
                        btmp.a=copy.deepcopy(board.a)
                        btmp.a[k[1]-1][k[0]-1]=btmp.a[i][j]
                        btmp.a[i][j]=None
                        if(bmatecond(btmp)==0):
                            return 0
                    for k in checkt(board,ptmp,0)[1]:
                        btmp=chessboard()
                        btmp.a=copy.deepcopy(board.a)
                        btmp.a[k[1]-1][k[0]-1]=btmp.a[i][j]
                        btmp.a[i][j]=None
                        if(bmatecond(btmp)==0):
                            return 0
        return 'b'
    ################## white #################
    if(bmatecond(board)=='w'):
        for i in range(8):
            for j in range(8):
                if(board.a[i][j]!=None and board.a[i][j][0]=='w'):
                    ptmp=pieces()
                    ptmp.type=board.a[i][j][1:len(board.a[i][j])-1]
                    ptmp.id=board.a[i][j]
                    ptmp.side='w'
                    ptmp.x=j+1
                    ptmp.y=i+1
                    for k in checkt(board,ptmp,0)[0]:
                        btmp=chessboard()
                        btmp.a=copy.deepcopy(board.a)
                        btmp.a[k[1]-1][k[0]-1]=btmp.a[i][j]
                        btmp.a[i][j]=None
                        if(wmatecond(btmp)==0):
                            return 0
                    for k in checkt(board,ptmp,0)[1]:
                        btmp=chessboard()
                        btmp.a=copy.deepcopy(board.a)
                        btmp.a[k[1]-1][k[0]-1]=btmp.a[i][j]
                        btmp.a[i][j]=None
                        if(wmatecond(btmp)==0):
                            return 0
        return 'w'
    return 0