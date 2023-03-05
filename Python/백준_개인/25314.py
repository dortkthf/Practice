import sys
input = sys.stdin.readline

n = int(input())
a = n//4
ans = ''
for i in range(a):
    ans+='long '

ans+='int'
print(ans)