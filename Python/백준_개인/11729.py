n = int(input())
def hanoi(n,a,b,c):
    if n == 1:
        print(a,c)
    else:
        hanoi(n-1,a,b,c)
        hanoi(1,a,b,c)
        hanoi(n-1,b,a,c)
print(2**n-1)
hanoi(n,1,2,3)