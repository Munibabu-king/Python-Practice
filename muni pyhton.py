#removal of special character
'''a=input()#removal of special character
clean=''
for i in a:
    if i.isalnum():
        clean+=i
print(clean)
'''
'''
a=input()
clean=''
for i in a:
    print(i)
''''''
a="123456"
z=[x for x in a]
print(' '.join(z[::-1]))
''''''
#string sentence convertere
m="muni babu hero is man"
m=m.split()
print(' '.join(i[::-1]for i in m))
''''''
evenodd=[2,3,4,5]
[print(f"even{i}")for i in evenodd if i%2==0]
'''
evenodd=[2,3,4,5]
[print(f"even {evenodd[i]}")if evenodd[i]%2==0  else print(f"odd {evenodd[i]}")for i in range(len(evenodd))]
