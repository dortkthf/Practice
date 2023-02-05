n,k = map(int,input().split())
values = [int(input()) for i in range(n)]
values.sort(reverse=True)
# print(values)
cnt = 0
for i in values:
    if i <= k:
       cnt+=k//i
       k%=i
print(cnt) 