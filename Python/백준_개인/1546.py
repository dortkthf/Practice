n = int(input())
exams = list(map(int,input().split()))
max_exam = max(exams)
sum_new_exams = 0
for sub in exams:
    sum_new_exams+=(sub/max_exam)*100
print(sum_new_exams/n)