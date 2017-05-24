print 'please enter an integer biger then 3 :'
n = input()
print "---------"
x = 1
y = 1
i = 3
print x
print y
while i <= n:
	z = x + y
	print z 
	x = y
	y = z
	i += 1
