import copy, sys
input = sys.stdin.readline

n,b = map(int,input().split())
mtx = [list(map(int,input().split())) for i in range(n)]
ans = [[0 for i in range(n)] for i in range(n)]

def cal(tmp,tmp2):
    for k in range(n):
        for i in range(n):
            res = 0
            for j in range(n):
                res+=(tmp[k][j]*tmp2[j][i])
            res%=1000
            ans[k][i] = res
    return

def power(mtx,b):
    global ans
    tmp = copy.deepcopy(mtx)

    if b == 1:
        return
    elif b%2 == 0:
        cal(tmp,tmp)
        power(ans,b//2)
        return
    elif b%2 != 0:
        q = copy.deepcopy(mtx)
        cal(tmp,tmp)
        power(ans,b//2)
        ans2 = copy.deepcopy(ans)
        cal(ans2,q)
        return

power(mtx,b)

if b == 1:
    for i in range(n):
        for j in range(n):
            mtx[i][j]%=1000
    for i in mtx:
        print(*i,sep=' ')
else:
    for i in ans:
        print(*i,sep=' ')