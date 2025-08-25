# 23334444234  -> 234234
'''a=input()
ch=''
a=[int(i)for i in a]
ch+=str(a[0])
for i in range(1,len(a)):
    if a[i]==a[i-1]:
        continue
    else:
        ch+=str(a[i])
print(ch)'''

'''a="123345645678564455555577"
ch=''
ch+=a[0]
for i in range(1,len(a)):
    if a[i]==a[i-1]:
        continue
    else:
        ch+=a[i]
print(ch)
        '''
