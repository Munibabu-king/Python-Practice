s=input()
s=list(s)
k=[]
for i in range((len(s)-1),-1):
    k.append(s[i])
print(''.join(k))
