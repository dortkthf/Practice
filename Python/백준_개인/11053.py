1 2 3 4 5 6 7 8 9 10
10
10

1 5 2 6 3 4 5 6 7 8 9 

4 7 9 1 2 3 4 5 6 7 10

4 7 8 9 10 11 12 13 1 2 3

4 7 8 9 10 1 2 3 4 5 6 7 8 9 10 11 12

n = int(input())
a = list(map(int,input().split()))

l1 = []
p1 = 0
n1 = 0

l2 = []
p2 = 0
n2 = 0
for an in a:
    if an > n1:
        p1 = n1
        n1 = an
        l1.append(n1)
    elif an > p1 and an < n1:
        n1 = an
        l1.pop()
        l1.append(n1)        
    elif an < min(l1):
        if an > n2:
            p2 = n2
            n2 = an
            l2.append(n2)
        elif an < n2 and p2 < an:
            n2=an
            l2.pop()
            l2.append(n2)
        if 
        l2.append(n2)
    if n2 != 0:
        if an > n2:
            p1 = n2
            n2 = an

            