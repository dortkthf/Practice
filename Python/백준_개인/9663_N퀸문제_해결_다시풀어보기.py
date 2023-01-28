import sys
input = sys.stdin.readline

n = int(input())

row = [0 for i in range(n)]
find = [0 for i in range(n+1)]
find2 = [0 for i in range(2*n+1)]
ans = 0

def n_queens(x):
    global ans, find, find2
    if x == n:
        ans+=1
        return
    for i in range(n):
        if find[i] == 1 or find2[i+x] == 1:
            continue
        row[x] = i
        for j in range(x):
            if row[j] == row[x] or abs(row[x]-row[j]) == abs(x-j):
                break
        else:
            find[i] = 1
            find2[i+x] = 1
            n_queens(x+1)
            find[i] = 0
            find2[i+x] = 0

n_queens(0)
print(ans)