# magic_square = [ 
# 	[8, 3, 4],
# 	[1, 5, 9],
# 	[6, 7, 2]
# ]

# print type(magic_square)
# print type(magic_square[0])
# print type(magic_square[1])
# print type(magic_square[2])

# print sum(magic_square[0])
# print sum(magic_square[1])
# print sum(magic_square[2])

# Question nested list
# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# new_list = []
# for i in list1:
# 	if i not in list2:
# 		new_list.append(i)
# print new_list

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]
# ]
# # a = sum(marks[0])
# # b = sum(marks[1])
# # c = sum(marks[2])
# # print a+b+c
# total = 0
# for i in range(len(marks)):
# 	for j in marks[i]:
# 		total+=j
# print total

# total = 0
# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ]
# for i in range(len(marks)):
# 	for j in marks[i]:
# 		total+=j
# print total

marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
]
total = 0
for i in range(len(marks)):
	for j in marks[i]:
		total+=j
print total
