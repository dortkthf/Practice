n,m = map(int,input().split())

ls = list(i for i in range(1,n+1))

s = []

def sol():
    for i in ls:
        if len(s) == 0:
            s.append(i)
        elif s[-1] <= i:
            s.append(i)
        else:
            continue

        if len(s) == m:
            print(*s)
            s.pop()
            continue
        sol()
        s.pop()        
sol()