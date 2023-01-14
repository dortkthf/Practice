import sys
input = sys.stdin.readline

n = int(input())
res = [0 for i in range(n+1)]
for i in range(1,n+1):
    if i == 1:
        res[i] = 1
    elif i == 2:
        res[i] = 2
    else:
        res[i] = res[i-1]%15746+ res[i-2]%15746

print(res[n]%15746)