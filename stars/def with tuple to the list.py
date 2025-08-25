'''def my_tuple_convert(tuple_m,number):
    tuple_n=list(tuple_m)
    tuple_n.append(number)
    tuple_m=tuple(tuple_n)
    return tuple_m
tuples=(1,2,3,4,5)
numbers=4
tuple_m=my_tuple_convert(tuples,numbers)
print(tuple_m)'''

k=('muni','babu','hii')
m=list(k)
m.insert(2,'ni')
k=tuple(m)
print(k)
