s=input()
s1=''
for i in s:
    if i in s1:
        continue
    else:
        s1+=i
print(s1)
