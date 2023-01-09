# 1. 직접구현 

# import sys, math
# input = sys.stdin.readline
# res = []
# t = int(input())
# for _ in range(t):
#     a,b = map(int,input().split())
#     al = []
#     for i in range(1,int(math.sqrt(a))+1):
#         if a%i == 0:
#             al.append(i)
#             al.append(a//i)
#     al.sort(reverse=True)

    
#     bl = []
#     for i in range(1,int(math.sqrt(b))+1):
#         if b%i == 0:
#             bl.append(i)
#             bl.append(b//i)
#     bl.sort(reverse=True)

#     for i in al:
#         if i in bl:
#             gcd = i
#             break
#     res.append((int(a*b)//gcd))
# print(*res, sep='\n')

# 2. 파이썬 math라이브러리 사용
import sys, math
input = sys.stdin.readline
t = int(input())
res = []
for _ in range(t):
    x,y = map(int,input().split())
    res.append(math.lcm(x,y))
print(*res, sep='\n')