#1
'''1).
v=int(input("no of total vehicles"))
w=int(input("total no of wheels"))
fw=int((w-2*v)/2)  #no of four wheeler vehicles
tw=int(v-fw)      #no of 2 wheeler vehicles
print(f'tw->{tw},Fw->{fw}')'''
#2
'''m=input()
if m.count('#')!=m.count('*'):
    print("not valid")
else:
    print('valid')'''
#3
'''s=input()[1:-1]
k=[int(i)for i in s.split(',')if i.isdigit()]
count=1
for i in range(1,len(k)):
    if max(k[:i])<=k[i]:
        count+=1
print(count)
        '''
#4
'''rows=int(input())
cols=int(input())
mat=[]
for i in range(rows):
    l=[]
    for m in range(cols):
        k=int(input())
        if k!=0 and k!=1:
            print("enter only 0 or 1")
            exit()
        else:
            l.append(k)
    mat.append(l)
c=[]
for i in mat:
    c.append(i.count(1))
print(f'{max(c)}->{c.index(max(c))+1}')'''
#5
'''arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr2=[-abs(i)for i in arr2]
sumi=0
k=[]
for i in range(len(arr1)):
    sumi+=arr1[i]+arr2[i]
    k.append(sumi)
print(max(k))'''
               
#6
arc=list(map(str,input().split()))
for i in arc:
    if (arc.count(i)%2!=0):
        print(i)
        break
else:
    print("all are even")
        
    
    
            
        
