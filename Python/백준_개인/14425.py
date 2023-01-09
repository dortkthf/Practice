# import sys 를 사용하면 훨씬 빠르게 입력받을수 있다.
# import sys X 904ms
# import sys O 124ms

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
S = set(input().rstrip() for i in range(n))
N = list(input().rstrip() for i in range(m))
cnt = 0
for i in N:
    if i in S:
        cnt+=1
print(cnt)