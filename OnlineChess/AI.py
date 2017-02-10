from OnlineChess.classes import chessboard,pieces
from OnlineChess.moving import checkt
def nextstep(board):
    for i in range(8):
        for j in range(8):
            if(board.a[i][j]!=None):
                p=pieces()
                p.x=j+1
                p.y=i+1
                p.type=board.a[i][j][1:len(board.a[i][j])-1]
                p.id=board.a[i][j]
                p.side='b'
                if(checkt(board,p)[0]):
                    return ((j+1,i+1),checkt(board,p)[0][0])
                if(checkt(board,p)[1]):
                    return ((j+1,i+1),checkt(board,p)[1][0])
