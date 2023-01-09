n = int(input())
sol = list(map(int,input().split()))
sol.sort()
if n == 1:
    print(sol[0]**2)
else:
    print(sol[0]*sol[-1])    