# 세트함수로 중복을 제거한후 딕셔너리를 이용해서 해당 수와 인덱스를 넣어서 
# 해당 수의 인덱스 값이 자신보다 작은 값들의 갯수임을 이용

import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int,input().split()))
ls2 = sorted(list(set(ls)))
ls3 = {ls2[i]: i for i in range(len(ls2))}
for i in ls:
    print(ls3[i],end=' ')
