my_list=input().split()
m=int(input("enter the place of that element:"))
print(my_list)
my_list = [int(i) for i in my_list]
my_list = [i.replace(',', '') for i in my_list]
print(my_list)
