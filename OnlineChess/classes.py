class pieces:
    x=1
    y=1
    type='rook'
    id='brook1'
    side='w'
    #white ='w'  Black='b'
class chessboard:
    turn='w'
    #white =w Black =b
    a=[[None for _ in range(8)] for i in range(8)]
    a[0][0]='brook1'
    a[0][1]='bknight1'
    a[0][2]='bbishop1'
    a[0][3]='bqueen1'
    a[0][4]='bking1'
    a[0][5]='bbishop2'
    a[0][6]='bknight2'
    a[0][7]='brook2'
    a[1][0]='bpawn1'
    a[1][1]='bpawn2'
    a[1][2]='bpawn3'
    a[1][3]='bpawn4'
    a[1][4]='bpawn5'
    a[1][5]='bpawn6'
    a[1][6]='bpawn7'
    a[1][7]='bpawn8'
    a[6][0]='wpawn1'
    a[6][1]='wpawn2'
    a[6][2]='wpawn3'
    a[6][3]='wpawn4'
    a[6][4]='wpawn5'
    a[6][5]='wpawn6'
    a[6][6]='wpawn7'
    a[6][7]='wpawn8'
    a[7][0]='wrook1'
    a[7][1]='wknight1'
    a[7][2]='wbishop1'
    a[7][3]='wqueen1'
    a[7][4]='wking1'
    a[7][5]='wbishop2'
    a[7][6]='wknight2'
    a[7][7]='wrook2'
