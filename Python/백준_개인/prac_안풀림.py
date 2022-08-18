citations = [3, 0, 0, 1, 5, 4, 0,10,11,12]

def index(citations):
    result = []
    for num1 in citations:
        tmp = 0
        dtmp = 0
        for num2 in citations:
            if num1<=num2:
                tmp+=1
            if num1>num2:
                dtmp+=1
        if tmp>=num1>=dtmp:
            result.append((num1))
    if result:
        return max(result), result
    else:
        return 0
print(index(citations))
