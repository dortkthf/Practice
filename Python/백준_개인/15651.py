n,m = map(int,input().split())

nums = list(i for i in range(1,n+1))

s = []
def sol():
    for i in nums:
        s.append(i)
        if len(s) == m:
            print(*s)
            s.pop()
            continue
        sol()
        s.pop()
sol()