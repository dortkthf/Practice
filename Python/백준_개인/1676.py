def fac(n):
    ans = 1
    for i in range(2,n+1):
        ans*=i
    return ans

n = int(input())
fn = fac(n)

fns = str(fn)[::-1]

cnt = 0
for i in fns:
    if i == '0':
        cnt+=1
    else:
        print(cnt)
        break