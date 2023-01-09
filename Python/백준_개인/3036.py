# 1. fractions 모듈을 활용한 분수표현식 
# print에서 sep와 end의 차이

from fractions import Fraction

n = int(input())
ring = list(map(int,input().split()))
for i in range(1,n):
    a = Fraction(ring[0],ring[i])
    print(a.numerator,a.denominator,sep='/')

# 2. 최대 공약수로 나눈값으로 표현하기

import math

n = int(input())
ring = list(map(int,input().split()))
for i in range(1,n):
    gcd = math.gcd(ring[0],ring[i])
    print(ring[0]//gcd,ring[i]//gcd,sep='/')
