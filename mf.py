a=list(map(int,input().split()))
sumi=[]
for i in range(len(a)):
    for j in range(i,len(a)):
        sumi.append(a[j:])
print(max(sumi))

