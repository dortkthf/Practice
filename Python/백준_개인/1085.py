x,y,w,h = map(int,input().split())
res = [x,y,w-x,h-y]
print(min(res))