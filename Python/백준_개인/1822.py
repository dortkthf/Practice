na,nb = map(int,input().split())
anums = set(list(map(int,input().split())))
bnums = set(list(map(int,input().split())))
result = sorted(list(anums-bnums))
if len(result):
    print(len(result))
    print(*result)
else:
    print(0)