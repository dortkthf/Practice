num = int(input())
p_num = list(map(int,input().split()))
p_num_list = []
for i in range(23) :
    p_num_list.append(0)
    
for i in range(num) :
    p_num_list[p_num[i]-1]+=1

for i in range(23) :    
    print(p_num_list[i],end=' ')
