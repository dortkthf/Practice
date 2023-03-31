import sys
input = sys.stdin.readline

p = ['ChongChong']
cnt = 1

n = int(input())
for i in range(n):
    a,b = list(input().split())
    if a in p and b not in p:
        p.append(b) 
        cnt+=1
    elif b in p and a not in p:
        p.append(a)
        cnt+=1

print(cnt)