import sys, copy
input = sys.stdin.readline

n = int(input())

matx = [[1,1],[1,0]]

p = 1000000007

ans = [[0,0],[0,0]]

def cal(matx1,matx2):
    
    for k in range(2):
        for i in range(2):
            res = 0
            for j in range(2):
                res+=matx1[k][j]*matx2[j][i]
            res%=p
            ans[k][i] = res
    return

def find(matx,n):
    global ans
    q = copy.deepcopy(matx)

    if n == 1:
        return
    elif n%2 == 0:
        cal(q,q)
        find(ans,n//2)
        return
    elif n%2 != 0:
        cal(q,q)
        find(ans,n//2)
        tmp = copy.deepcopy(ans)
        cal(q,tmp)
        return

find(matx,n)
if n == 1:
    print(1)
else:
    print(ans[1][0])