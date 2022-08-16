t = int(input())
for _ in range(t):
    n, word = input().split()
    p = ''
    for i in word:
        p+=i*int(n)
    print(p)