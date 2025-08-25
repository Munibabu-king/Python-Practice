n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
min_num=float('inf')
for i in range(n):
    current_sum=sum(a[:i+1])
    if(current_sum < min_num):
        min_num=current_sum
print(min_num)
