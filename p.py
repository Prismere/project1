s='python programming'
l=len(s)
print('length is',l)
print(s[7:14])
print(3*s)
for c in s:
	print(c)
d=list(s)
print(d)
print(s[3])
print(s[5:9])
for i in range(len(s)-2):
	print(s[i])
h='lab exercises 2013'
print(s+h)
t=s+h
r=t.replace('e','c')
print(r)
g=t.split('0')
print(g)
q=''
for w in list(g):
	q=q+'#'+w
print(q[1:])
#print(q)
print(t.count(''))
z=0
for c in t:
	if c in '0123456789':
		z=z+1
print(z)
n=0
for c in t:
	if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
		n=n+1
print(n)
print (t.capitalize() )
print(t.upper())
c=s.ljust(50,' ')
print(c)
d=s.rjust(50,' ')
print(d)
