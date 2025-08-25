a=int(input())
rev=0
while a>0:
    rev=rev+(a%10)
    a=a//10
print(rev)
