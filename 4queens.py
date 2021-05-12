import numpy as np

def iscolumn_available(n, p, occupied):
    for i in range(n):
        if occupied[i][p] == 1:
            return False
    return True


def isrow_available(n, p, occupied):
    for i in range(n):
        if occupied[p][i] == 1:
            return False
    return True

def isdiagonal_available(n, pi, pj, occupied):
    ti = pi
    tj = pj
    # print("up right")
    while(1):
        # print(ti, tj)
        if occupied[ti][tj] == 1:
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
        if occupied[ti][tj] == 1:
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
        if occupied[ti][tj] == 1:
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
        if occupied[ti][tj] == 1:
            return False
        if ti == n-1 or tj == n-1:
            break
        ti += 1
        tj += 1
    return True


def queen(si, sj, n, occupied):
    print("si & sj", si, sj)
    if iscolumn_available(n, sj, occupied) and isrow_available(n, si, occupied) and isdiagonal_available(n, si, sj, occupied):
        occupied[si][sj] = 1
        return 1
    return 0
    


n = 4
occupied = np.zeros((n, n))
# print("before")
# print(occupied)
count = 0
# occupied[0][0] = 1 # No solution
# occupied[0][1] = 1 # Solution
occupied[0][2] = 1 # Solution
# occupied[0][3] = 1 # No Solution

# No Recursion 
for i in range(n):
    for j in range(n):
        if queen(i, j, n, occupied) == 1:
            count += 1

print("after")
print(occupied)
if count+1 == n:
    print("Solved")
else:
    print("No Solution")
