# import sys
# input = sys.stdin.readline

# n,b = input().split()

# c = '0123456789'
# d = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# e = 10
# dic = {}

# for i in c:
#     dic[i] = int(i)

# for i in d:
#     dic[i] = e
#     e+=1

# n = n[::-1]

# ans = 0
# cnt = 0

# for i in n:
#     ans += dic[i]*(int(b)**cnt)
#     cnt+=1

# print(ans)

# import sys
# input = sys.stdin.readline

# a = list(input().split())
# n,b = a[0], int(a[1])

# nn = len(n)
# ans = 0

# for i in range(nn):
#     if n[i].isdigit():
#         ans += int(n[i])*(b**(nn-1-i))
#     else:
#         ans += (ord(n[i])-55)*(b**(nn-1-i))

# print(ans)