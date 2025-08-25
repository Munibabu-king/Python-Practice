#linear
a=int(input())
l=[]
for i in range(a):
    b=int(input())
    l.append(b)
x=int(input("serch elemnt:"))
for i in l:
    if x==i:
        print(l.index(i))
        break
