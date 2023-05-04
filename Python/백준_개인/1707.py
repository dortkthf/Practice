from collections import deque

k = int(input())
for _ in range(k):
    v,e = map(int,input().split())
    graph = [[] for i in range(v+1)]
    queue1 = deque()
    queue = deque()
    
    for i in range(e):
        b,a = map(int,input().split())
        if i == 0:
            queue.append(a)
            queue.append(b)
        graph[b].append(a)
        graph[a].append(b)
        queue1.append(b)
        queue1.append(a)
    queue1 = set(queue1)
    queue1 = deque(queue1)
    

    check = list(0 for i in range(v+1))
    check[queue[0]] = -1
    check[queue[1]] = 1
    res = True
    while queue:
        num = queue.popleft()
        opposite = graph[num]
        ck = check[num]
        if ck == 0:
            ck = 1
        for i in opposite:
            if ck == 1:
                if check[i] == 0:
                    check[i] = -1
                    queue.append(i)
                elif check[i] == 1:
                    res = False
                    break
            elif ck == -1:
                if check[i] == 0:
                    check[i] = 1
                    queue.append(i)
                elif check[i] == -1:
                    res = False
                    break
        if res == False:
            break
        # if len(queue) == 0:
        #     queue=queue1
    print(res)
        