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
    
