'''n=int(input())
count=0
sum=0
while n>0:
    rem=n%10
    sum+=rem
    n//=10
    count+=1
print(count)
while count >0:
    k=count-1
    count-k
print(sum)'''

'''a,b,c=list(map(str,input().split(" ")))

if (b=='+'):
    print(int(a)+int(c))
elif (b=='-'):
    print(int(a)-int(c))
elif (b=='*'):
    print(int(a)*int(c))
elif (b=='/'):
    if(int(c)==0):
        print("error")'''
'''k=int(input())
b=''
while k>0:
    rem=k%2
    b=str(rem)+b
    k//=2
print(b.count('1'))

'''
'''n=int(input())
fact=1
while'''
        
'''a=list(map(int,input().split()))
print(a[::-1])'''
a=input()[1:-1]
a=a.replace(" ","")
print(list(map(int,a.split(",")))[::-1])
r=list(map(int,input()[1:-1].split(", ")))

if(y%100):
    if(y%400):
        print("leap")
    else:
        print("not")
else:
    if(y%4==0):
        print("leap")



