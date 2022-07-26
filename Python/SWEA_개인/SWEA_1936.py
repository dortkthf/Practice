a, b = map(int,input().split())

# 가위 1, 바위 2, 보 3

if a == 1 and b == 3:
    print('A')
elif a == 2 and b == 1 :
    print('A')
elif a == 3 and b ==2 :
    print('A')
else :
    print('B')