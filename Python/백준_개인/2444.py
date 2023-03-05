import sys
input = sys.stdin.readline

n = int(input())
total = 2*n-1

for i in range(1,2*n):

    if i > n:
        c = i-n
        a = 2*n-1-c*2
        b = (total-a)//2
        star = ' '*b+a*'*'
        print(star)
        continue    
    a = 2*i-1
    b = (total-a)//2
    star = ' '*b+a*'*'
    print(star)