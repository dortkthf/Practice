### lines = sys.stdin.readline() 로받기

import sys
lines = sys.stdin.readlines()

for line in lines:
    a,b = map(int,line.split())
    print(a+b)

### try except 문으로 받기

# while True:
#     try:
#         a,b = map(int,input().split())
#         print(a+b)
#     except:
#         break
    