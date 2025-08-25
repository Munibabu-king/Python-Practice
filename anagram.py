'''a=list(map(int,input().split()))
avg=sum(a)/len(a)
k=[]
for i in range(len(a)):
    k.append(pow((avg-a[i]),2))
print(f'{(sum(k)/len(k))**0.5:.2f}')'''

a=list(map(int,input().split()))
avg=sum(a)/len(a)
b=(((sum((avg-i)**2 for i in a)/len(a))**0.5))
print(f'{b:.2f}')
