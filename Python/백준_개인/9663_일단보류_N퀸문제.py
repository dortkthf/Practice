import sys
input = sys.stdin.readline

n = int(input())

row = [0 for i in range(n)]
ans = 0

def n_queens(x):
    global ans
    if x == n:
        ans+=1
        return
    for i in range(n):
        row[x] = i
        if promising(x):
            n_queens(x+1)

def promising(x):
    for i in range(x):
        if row[i] == row[x] or abs(row[x]-row[i]) == abs(x-i):
            return False
    return True

n_queens(0)
print(ans)