num=int(input("enter a number"))
num1=0
print(num1,end=" ")
num2=1
print(num2,end=" ")
for i in range(2,num+1):
   num3=num2
   num1=num2
   num2=num3+1
   print(f"{num2}",end=" ") 
