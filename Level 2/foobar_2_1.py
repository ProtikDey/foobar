import math

def posToCoOrd(pos):
    x = int(math.floor(pos/8))
    y = int(pos%8)
    return (x,y)

def coOrdToPos(x,y):
    return x+y*8

def getAllMoves(x,y):
    all_moves=[]
    valid_moves=[]

    all_moves.append((x+2, y+1))
    all_moves.append((x+2, y-1))
    all_moves.append((x-2, y+1))
    all_moves.append((x-2, y-1))
    all_moves.append((x+1, y+2))
    all_moves.append((x+1, y-2))
    all_moves.append((x-1, y+2))
    all_moves.append((x-1, y-2))

    for (x,y) in all_moves:
        if(x >= 0 and x < 8 and y >= 0  and y < 8):
            valid_moves.append((x,y))

    return valid_moves

def solution(src, dest):
    if src==dest:
        return 0
    
    src_x,src_y=posToCoOrd(src)
    dest_x,dest_y=posToCoOrd(dest)

    allMoves=getAllMoves(src_x,src_y)
    depth_move=[]

    moves=0

    while True:
        moves+=1

        for move in allMoves:
            if move[0]==dest_x and move[1]==dest_y:
                return moves
            depth_move.extend(getAllMoves(move[0],move[1]))
        allMoves=depth_move
        depth_move=[]

if __name__ == '__main__':
    sol = solution(19,36)
    print(sol)