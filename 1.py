'''num=int(input("number"))
c=""
while num>0:
    r=num%2
    c=str(r)+c
    num//=2
print(c)'''
'''n=int(input("enter number"))# serie before index number like 22numbers,12numbers
n1=0
print(n1)
n2=1
print(n2)
count=0
while (count< (n-2)):
    temp=n1+n2
    print(temp)
    n1=n2
    n2=temp
    count+=1'''
'''n=int(input("enter number"))# the number is in fibinocci or not
n1=0
n2=1
l=[n1,n2]
while n2<n:
    temp=n1+n2
    n1=n2
    n2=temp
    l.append(n2)
if n in l:
    print(l.index(n))
else:
    print("not found")'''
'''n=int(input("enter number"))#series before original fibinocci number like before 15 number
n1=0
print(n1)
n2=1
print(n2)
count=0
while n>n2:
    temp=n1+n2
    if temp<n:
        print(temp)
    n1=n2
    n2=temp
    count+=1'''
'''n=int(input())
n1=0
n2=1
count=0
if(n==1):
    print(n1)
elif(n==2):
    print(n1)
    print(n2)
elif(n>2):
    print(n1)
    print(n2)
    while count< (n-2):
        temp=n1+n2
        print(temp)
        n1=n2
        n2=temp
        count+=1
else:
    print("not possible")'''
'''n=int(input())
n1=0
n2=1
count=0
if(n==1):
    print(n1)
elif(n>=2):
    while count<n:
        temp=n1+n2
        if (temp==n):
            print(count+3)
            break
        n1=n2
        n2=temp
        count+=1
    else:
        print("not there")'''
'''n=int(input())  #decimal to binary
l=[]
while n>0:
    rem=n%2
    l.append(rem)
    n//=2
l=l[::-1]
l=[str(i)for i in l]
print(''.join(l))'''


'''note :
    a="rtyuiop"
    a=[1:-5]  is --> -5 is (len(a)-5)=7-5=2
    ex: [-7,-4]......-4 only len(a)-4=3'''

'''a=input().lower()
vow="aeiou"
i=0
c=''
while (i<len(a)):
    if vow[i]in a:
        k=(vow[i]*(a.index(i)+1))
        c=c+str(k)
        i+=1
    else:
        c=c+a[i]
        i+=1
print(c)'''
'''d=int(input())
a=0
while(a<d):
    print("*"*(a+1))
    a+=1'''

d=int(input())
a=0
jk=''
while(a<d):
    jk=jk+(' '*(d-a-1)+'* '*(a+1)).rstrip()+"\n"
    a+=1
print(jk)
        

    


