from audioop import avg


t = int(input())
for _ in range(t):
    num = list(map(int,input().split()))
    numbers = num[0]
    scores = num[1:]
    averg = sum(scores)/numbers
    cnt = 0
    for score in scores:
        if score > averg:
            cnt+=1
    print('%.3f'%(cnt/numbers*100)+'%')
    