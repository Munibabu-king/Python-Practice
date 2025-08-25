list=['342','hello','hai']
y=[]
for i in list:
    y.append(len(i))
z=max(y)
print(z)
value=y.index(z)
string=list[value]
print(string)
