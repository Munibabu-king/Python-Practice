a=input()
a=list(a)
k=a
k.reverse()
m=[]
l=[]
count=0
for i in range(len(a)):
    if a[i]==k[i]:
        count+=1
        continue
    else:
        l.append(k[:i])
if count==len(a):
    l.append(k[::])
if len(m)<len(l):
    m=l
print(m)
        
    
        
