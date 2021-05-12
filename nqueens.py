import numpy as np

def iscolumn_available(n, p, board):
    for i in range(n):
        if board[i][p] == 1:
            return False
    return True


def isrow_available(n, p, board):
    for i in range(n):
        if board[p][i] == 1:
            return False
    return True
def isdiagonal_available(n, pi, pj, board):
    ti = pi
    tj = pj
    # print("up right")
    while(1):
        # print(ti, tj)
        if board[ti][tj] == 1:
            return False
        if ti == 0 or tj == n-1:
            break
        ti -= 1
        tj += 1
    ti = pi
    tj = pj
    # print("down left")
    while(1):
        # print(ti, tj)
        if board[ti][tj] == 1:
            return False
        if ti == n-1 or tj == 0:
            break
        ti += 1
        tj -= 1
    ti = pi
    tj = pj
    # print("up left")
    while(1):
        # print(ti, tj)
        if board[ti][tj] == 1:
            return False
        if ti == 0 or tj == 0:
            break
        ti -= 1
        tj -= 1
    
    # print("down right")
    ti = pi
    tj = pj
    while(1):
        # print(ti, tj)
        if board[ti][tj] == 1:
            return False
        if ti == n-1 or tj == n-1:
            break
        ti += 1
        tj += 1
    return True

# def check_3x3():



def queen(n, N, board):
    print(n)

    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            # Dynamic program to reduce computational time // memoize technique.
            
            if iscolumn_available(N, j, board) and isrow_available(N, i, board) and isdiagonal_available(N, i, j, board):
                board[i][j] = 1
                if queen(n-1, N, board)==True:
                    return True
                board[i][j] = 0

    return False

q = 8
board = np.zeros((q, q))
queen(q, q, board)
print(board)