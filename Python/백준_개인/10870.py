n = int(input())
memo = [0]*(n+1)

def fibonacci(n):
    if n == 0 or n == 1:
        memo[n] = n
    elif memo[n] == 0:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]
print(fibonacci(n))