pro = [list(map(int,input().split())) for i in range(9)]
ans = 0
zro = 0
res = [0 for i in range(2)]
for i in range(9):
    for j in range(9):
        zro+=pro[i][j]
        if pro[i][j] > ans:
            ans = pro[i][j]
            res[0] = i+1
            res[1] = j+1
        if zro == 0:
            ans = 0
            res[0] = 1
            res[1] = 1

print(ans)
print(*res)