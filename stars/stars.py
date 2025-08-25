k=int(input("enter no.of rows:"))
for i in range(1,k+1):
    print("  "*(k-i)+" * "*i)
for i in range(k-1,0,-1):
    print("  "*(k-i)+"* "*i)

for i in range(1,k+1):
    print("* "*i+""*(k-i))
for i in range(k-1,0,-1):
    print("* "*i+""*(k-i))
