res = [0 for i in range(123456*2+1)]
for i in range(2,123456*2+1):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        res[i] = 1
        
while True:
    p = int(input())

    if p == 0:
        break
    
    print(sum(res[p+1:2*p+1]))
    
# 에라토스테네스의 체 설정 - 소수의 배수는 소수가 아니다.
# res = [1 for i in range(123456*2+1)]
# for i in range(2,123456*2+1):
#     if res[i]:
#         for j in range(i*2, 123456*2+1, i):
#             res[j] = 0

# while True:
#     n = int(input())
#     if n == 0 :
#         break
#     print(sum(res[n+1:2*n+1]))