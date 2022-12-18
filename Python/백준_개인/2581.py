sosu = []
m = int(input())
n = int(input())
for i in range(m, n + 1):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        sosu.append(i)
if sosu:
    print(sum(sosu))
    print(sosu[0])
else:
    print(-1)
