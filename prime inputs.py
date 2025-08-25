def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
prime=[]
n=2
k=int(input())
while len(prime)<=k:
    if is_prime(n):
        prime.append(n)
    n+=1
var1=prime[2]+prime[5]
var2=var1-1
print(prime)
print(var2)
    
