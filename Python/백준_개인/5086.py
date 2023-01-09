import sys
input = sys.stdin.readline

while True:
    x,y = map(int,input().split())
    if x == 0 and y == 0:
        break
    if y%x == 0 and x<y:
        print('factor')
    elif x%y == 0 and y<x:
        print('multiple')
    else:
        print('neither')    