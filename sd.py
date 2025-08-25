n=int(input())
a=input()[1:-1]
k=[int(i)for i in a.split(',')if i.isdigit()]
print(k)
if n!=len(k):
    print("value is not equal to the len of k")
else:
    sum=0
    for i in k:
        sum+=i
    mean=sum/len(k)
    h=[(mean-i)**2 for i in k]
    print(h)
    sumi=0
    for i in h:
        sumi+=i
    sumi/=n
    print(f'{round(sumi**0.5,2):.5f}')

