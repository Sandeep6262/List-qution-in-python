user=int(raw_input("input any number "))
total = 0
for j in range(1,user):
	add = ''
	for i in range(j):
		print 5,
		add+='5'
	print ''

	total=total+int(add)
print total