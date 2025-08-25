def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
def sum_number(numi):
    while numi>=10:
        numi=sum(int(i)for i in str(numi))
    return numi
m,n=map(int,input().split(','))
k=2
prime=[]
while len(prime)<=max(m,n):
    if is_prime(k):
        prime.append(k)
    k+=1

print(prime)
print(prime[m])
print(prime[n])
num1=prime[m]        
num2=prime[n]
result=sum_number(num1)*sum_number(num2)
print(result)
    
    
    
    
        
    
