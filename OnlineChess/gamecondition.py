from OnlineChess.moving import checkt
from OnlineChess.classes import pieces, chessboard
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
                if(bking in checkt(board,p)[1]):
                    return 'b'
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
                if (wking in checkt(board, p)[1]):
                    print(wking)
                    return 'w'
    return 0
def checkmatecond(board):
    ################## black #################
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
    if(bmatecond(board)=='b'):
        ptmp=pieces()
        ptmp.type='king'
        ptmp.id='bking1'
        ptmp.side='b'
        ptmp.x=bking[0]
        ptmp.y=bking[1]
        for i in checkt(board,ptmp)[0]:
            boardtmp=board
            boardtmp.a[bking[1]-1][bking[0]-1]=None
            boardtmp.a[i[1]-1][i[0]-1]='bking1'
            if(not bmatecond(boardtmp)):
                return 0
        return 'b'
    ################## white #################
    wking=(0,0)
    for i in range(8):
        tmp=0
        for j in range(8):
            if(board.a[i][j]=='wking1'):
                wking=(j+1,i+1)
                tmp=1
                break
        if(tmp):
            break
    if(wmatecond(board)=='w'):
        ptmp=pieces()
        ptmp.type='king'
        ptmp.id='wking1'
        ptmp.side='w'
        ptmp.x=wking[0]
        ptmp.y=wking[1]
        for i in checkt(board,ptmp)[0]:
            boardtmp=board
            boardtmp.a[wking[1]-1][bking[0]-1]=None
            boardtmp.a[i[1]-1][i[0]-1]='wking1'
            if(not wmatecond(boardtmp)):
                return 0
        return 'w'
