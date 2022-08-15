numbers = []
for _ in range(9):
    num = int(input())
    numbers.append(num)

num_max = max(numbers)
num_m_index = numbers.index(num_max)+1
print(num_max,num_m_index)