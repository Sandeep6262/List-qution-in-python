# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# add=0
# for i in numbers:
# 	add+=1
# print add


# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# gretar_20 = 0
# less_40 = 0
# for i in numbers:
# 	if i > 20:
# 		gretar_20+=1
# 	if i < 40:
# 		less_40+=1
# print "20 GRETAR THAN",gretar_20
# print "40 less than",less_40

# maximum numbers
# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# max_number = 0
# for i in numbers:
# 	if max_number < i:
# 		max_number = i
# print max_number

# second_max_number = 0
# for i in numbers:
# 	if i > second_max_number and max_number != i:
# 		second_max_number = i
# print second_max_number

places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
lengh = len(places)- 1
for i in range(len(places)):
	print places[lengh - i]