## 처음
sum_ = 0
scores = [int(input()) for i in range(10)]
for score in scores:
    sum_+=score
    if sum_>=100:
        if sum_-100>100-(sum_-score):
            print(sum_-score)
            break
        elif sum_-100<sum_-100-(sum_-score):
            print(sum_)
            break
        else:
            if sum_>sum_-score:
                print(sum_)
                break
            else:
                print(sum_-score)
                break
else:
    print(sum_)

## 두번째
sum_ = 0
scores = [int(input()) for i in range(10)]
for score in scores:
    sum_+=score
    if sum_>=100:
        if sum_-100>100-(sum_-score):
            print(sum_-score)
        else:
            print(sum_)
        break
else:
    print(sum_)
## 최종
sum_ = 0
scores = [int(input()) for i in range(10)]
for score in scores:
    sum_+=score
    result = sum_
    if sum_>=100:
        if sum_-100>100-(sum_-score):
            result = sum_-score
        else:
            result = sum_
        break
print(result)
