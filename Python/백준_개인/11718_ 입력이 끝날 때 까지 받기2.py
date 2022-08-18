## 출력 그대로 받기
result = []
while True:
    try:
        result.append(input())
    except:
        break
print(*result,sep='\n')


## EOFError 로 받기
while True:
    try:
        print(input())
    except EOFError:
        break