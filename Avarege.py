marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]

for i in marks:
	add = 0
	lengh = len(i)
	for j in i:
		add=add+j
	print "average",add/lengh