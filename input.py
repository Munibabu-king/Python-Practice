a=input()[1:-1]
arr=[]
for i in a:
    if i.isalpha():
        arr.append(i)
        
print(arr)
print(*arr)
