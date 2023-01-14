import sys
input = sys.stdin.readline

res = {}
for a in range(21):
    for b in range(21):
        for c in range(21):
            if a<=0 or b<=0 or c<=0:
                res[f'w({a}, {b}, {c})'] = 1
            elif a < b and b < c:
                res[f'w({a}, {b}, {c})'] = res[f'w({a}, {b}, {c-1})'] + res[f'w({a}, {b-1}, {c-1})'] - res[f'w({a}, {b-1}, {c})']
            else:
                res[f'w({a}, {b}, {c})'] = res[f'w({a-1}, {b}, {c})'] + res[f'w({a-1}, {b-1}, {c})'] + res[f'w({a-1}, {b}, {c-1})'] - res[f'w({a-1}, {b-1}, {c-1})']

while True:
    a,b,c = map(int,input().split())
    if a == -1 and b == -1 and c == -1:
        break
    if a<=0 or b<=0 or c<=0:
        print(f'w({a}, {b}, {c})',1, sep=' = ')
    elif a > 20 or b > 20 or c > 20:
        print(f'w({a}, {b}, {c})',res[f'w({20}, {20}, {20})'], sep=' = ')
    else:
        print(f'w({a}, {b}, {c})',res[f'w({a}, {b}, {c})'], sep=' = ')