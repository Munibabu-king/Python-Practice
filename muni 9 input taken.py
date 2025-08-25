#[2,3,4,5,6]
'''n=int(input())
arr=list(map(int,input().split()))
print(arr)
'''
'''n=input()
print(type(n))
arr=[]
for i in n:
    if i.isdigit()and ',':
        arr.append(int(i))
    else:
        continue
print(arr)
print(type(arr))'''
#multiple inputs taking x,y,z=[]
'''n,y=map(input().split(','))
print(n)'''
n, y = map(int, input().split(','))
print(n)
