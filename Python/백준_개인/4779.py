import sys
input = sys.stdin.readline

def kantor(n):
    a = 3**n
    if a == 1:
        return '-'
    b = kantor(n-1)
    c = (3**(n-1))*' '
    d = kantor(n-1)

    tmp = b+c+d
    return tmp

while True:
    try:
        n = int(input())
        print(kantor(n))
    except:
        break