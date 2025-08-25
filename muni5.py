#string values
'''k = 'munibib' 
ch = ''

for i in range(len(k)):
    if k[i] in 'aeiou':
      ch+=(k[i]*i)
    else:
        ch+=k[i]
print(ch)
        '''
'''else:
        ch += k[i]

print(ch)'''
'''
s='munuibaubu'
ch=''
ch+=s[0]
for i in range(1,len(s)):
	if s[i] in 'aeiou':
		k=s.index(s[i],i)
		ch+=(k+1)*s[i]
	else:
		ch+=s[i]
print(ch)
'''
