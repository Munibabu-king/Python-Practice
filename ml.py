n=int(input())
temp=n
sum=0
while temp>0:
    remainder=temp%10
    sum+=remainder**3
    temp=temp//10;
print(sum)
