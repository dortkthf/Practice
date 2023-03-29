n = int(input())
a = list(map(int,input().split()))
dic = {}
for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

a2 = [[0,0] for i in range(n)]

for i in range(n):
    a2[i][0] = dic[a[i]]
    a2[i][1] = a[i]

a2.reverse()

s = 0
for i in range(n):
    if i == 0:
        s = a2[i]
    else:
        if a2[i][0] < s[0]:
            a2[i] = s
        else:
            s = a2[i]
print(a2)