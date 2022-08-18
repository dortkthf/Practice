n = int(input())
def pac(n):
    if n==0:
        return 1
    else:
        return n*pac(n-1)
print(pac(n))