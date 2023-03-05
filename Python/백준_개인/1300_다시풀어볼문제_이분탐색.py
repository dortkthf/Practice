import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

# 이분탐색으로 모든 숫자들보다 작거나 같은 값들의 갯수를 구하는 방식 즉 k의 값과 이분탐색으로 찾은 개수의 값이 같은 답을 찾는것

def func(mid):
    ans = 0
    for i in range(1,n+1):
        ans += min(mid//i,n)
    return ans

def right(a):
    ans = False
    for i in range(2,n+1):
        if a%i == 0:
            ans = True
            return ans
    return ans        

def find(start,end):

    if end-start == 1:
        if func(start) == func(end):
            if right(start) == True:
                print(start)
                exit(0)
            print(end)
            exit(0)
        elif func(start) < k:
            print(end)
            exit(0)
        print(start)
        exit(0)
    
    mid = (start+end)//2

    start_c = func(start)
    mid_c = func(mid)

    if mid_c >= k and start_c <= k:
        find(start,mid)
        return
    end_c = func(end)
    if end_c >= k and mid_c <= k :
        find(mid,end)
        return
    
find(0,n*n)
