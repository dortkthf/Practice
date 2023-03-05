import sys, heapq
input = sys.stdin.readline

n = int(input())
x = list(int(input()) for i in range(n))
heap = []

for c in x:
    if c == 0:
        if len(heap) == 0:
            print(0)
            continue
        print(heapq.heappop(heap))
        continue
    heapq.heappush(heap,c)