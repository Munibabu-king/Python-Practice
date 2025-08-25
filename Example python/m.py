i=int(input("number of colmns"))
for k in range(i):
    for m in range(i):
        print(m*" "+i*"%",end=" ")
    print()
    i=i-1
