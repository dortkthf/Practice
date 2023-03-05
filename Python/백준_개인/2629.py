import sys
input = sys.stdin.readline

w = int(input())
wlst = list(map(int,input().split()))
m = int(input())
mlst = list(map(int,input().split()))

res = []
for i in mlst:
    if i > 15000:
        res.append('N')
        continue
    if i in wlst:
        res.append('Y')
        continue
    if i not in wlst:
        