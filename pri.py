'''n=int(input())
num1=0
num2=1
for i in range(n):
    print(num1)
    num1=num2
    num2=num1+num2
 ''' '''  
n = int(input())
a, b = 0, 1
for i in range(n):
    print(a)
    a,b=b,a+b

'''
#palindrome
n=int(input())
r=0
while (n >0):
    digit=n%10
    r=r*10+digit
    n=n//10
    
