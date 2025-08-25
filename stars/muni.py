def listt(x,y):
   x.append(y)
   return x
list_my=[20,30,45,67]
for element in range(2,10,2):
   m=listt(list_my,element)
print(m)
