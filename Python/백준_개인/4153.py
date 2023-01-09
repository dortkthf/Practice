import sys
input = sys.stdin.readline

while True:
    a,b,c = map(int,input().split())
    res = [a,b,c]
    res.sort()
    if res == [0,0,0]:
        break
    elif res[0]**2 + res[1]**2 == res[2]**2:
        print('right')
    else:
        print('wrong')