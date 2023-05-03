from collections import deque

n,m = map(int,input().split())

game = [i for i in range(101)]
check = [0 for i in range(101)]
check[1] = 1
queue = deque()
queue.append((1,0))

for i in range(n+m):
    x,y = map(int,input().split())
    game[x] = y

while queue:
    location, number = queue.popleft()
    if location == 100:
        print(number)
        exit(0)
    for i in range(1,7):
        if location+i > 100:
            continue
        elif check[location+i] == 0:
            queue.append((game[location+i],number+1))
            check[location+i] = 1