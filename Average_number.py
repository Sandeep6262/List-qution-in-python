# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]
# ]

# for i in marks:
# 	add = 0
# 	lengh = len(i)
# 	for j in i:
# 		add+=j
# 	print "year ka Avarage -",add/lengh

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ]
# for i in marks:
# 	add = 0
# 	lengh = len(i)
# 	for j in i:
# 		add+=j
# 	print "year ka Avarage -",add/lengh


# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78],
#     [87, 67, 49, 68, 88]
# ]
# for i in marks:
# 	add = 0
# 	lengh = len(i)
# 	for j in i:
# 		add+=j
# 	print "year ka Avarage -",add/lengh


# Q: How to find all pairs in an array of integers whose sum is equal to the given number?
# number = 30
# n = [10, 11, 12, 13, 14, 17, 18, 19]
# Output: [[11,19], [12,18]]

n = [10, 11, 12, 13, 14, 17, 18, 19]
new_list = []
for i in n:
	for j in n:
		if i + j == 30:
			if i not in new_list:
				new_list.append(i)
			if j not in new_list:
				new_list.append(j)
list1 = []
list2 = []
mix_list = []
add = 0
for i in new_list:
	if add == 4:
		break
	if i % 2 == 0:
		list1.append(i)
		add+=1
	else:
		list2.append(i)
		add+=1
mix_list.append(list2)
mix_list.append(list1)
print mix_list
	
