import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
a_dic = {}

for i in a:
    if i in a_dic:
        a_dic[i] += 1
    else:
        a_dic[i] = 1

a_count = [a_dic[i] for i in a]

stack = []
res = [0 for i in range(n)]
cnt = 0

for i in range(n):
    if i == 0:
        stack.append(i)
        cnt+=1
    else:
        if a_count[i] > a_count[stack[-1]] and a[i] != a[stack[-1]]:
            res[stack.pop()] = a[i]
            cnt-=1
        while True:
            if cnt > 0:
                if a_count[stack[-1]] < a_count[i] and a[stack[-1]] != a[i]:
                    res[stack.pop()] = a[i]
                    cnt-=1
                    continue
            break
        stack.append(i)
        cnt+=1
        
for i in stack:
    res[i] = -1
print(*res)