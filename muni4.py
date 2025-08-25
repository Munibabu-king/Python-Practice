k='muneibaebu'
ch=''
for i in k:
    if i in 'aeiou' not in ch:
        m=k.index(i)
        ch+=(i*m)
    else:
        ch+=i
print(ch)
