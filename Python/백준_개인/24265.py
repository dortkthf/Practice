import sys
input = sys.stdin.readline

n = int(input())
ans = (n/2)*(n-1)
print(round(ans),2,sep='\n')