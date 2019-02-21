var = str(raw_input("Input any name "))
lengh = len(var)-1
# print lengh
string = ''
for i in range(len(var)):
	string+=var[lengh-i]
if var == string:
	print "Polimdrome hai"
else:
	print "Not Polimdrome"

# var = str(raw_input("Input any name "))
# b = var[::-1]
# if var == b:
# 	print "Polimdrome hai"
# else:
# 	print "Not Polimdrome"
# 	