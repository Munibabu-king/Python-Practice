#zip
'''a={'muni',3,67,'babu'}
b={1,2,3,4}
h=['dsfgh',3,4,5,6]
for i,j,k in zip(a,b,h):
    print(f'{i} <- {j} -> {k}')'''
#enumarate     here enumarate,zip,sorted are used for tuple,string,list,set,dict

# but reversed used for only string,list,tuple not for set,dictionary
'''a='muni'
for i,j in enumerate(a):
    print(f'{i}->{j}')'''
#sorted
'''a=['muni','babu','herois','dfghjgfhjkl']
for i in sorted(a,key=len,reverse=True):
    print(f'{i}->{len(i)}')
print(max(a,key=len))'''
#reversed
a=['muni','babu','hero','dfgh']
print(' '.join(reversed(a)))
'''
a="munibabu is a hero material"
k=list(reversed(a))
print(k)
print(''.join(k))'''


