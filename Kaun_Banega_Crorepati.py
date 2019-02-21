question_list = [
	"1.How many continents are there?",  			# pehla question
	"2.What is the capital of India?",			# doosra question
	"3.NG mei kaun se course padhaya jaata hai?"	# teesra question
]
options_list = [
	#pehle question ke liye options
	["1.Four", "2.Nine", "3.Seven", "4.Eight"],
	#second question ke liye options
	["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
	#third question ke liye options
	["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]
]

life_line_list = [
	["1.Four","3.Seven",],
	["3.Chennai", "4.Delhi"],
	["1.Software Engineering", "2.Counseling"]
]

# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1]


# for i in range(len(question_list)):
# 	print "Aapka Sawaal hai:-"
# 	print question_list[i],"\n"
# 	print "Aapka options hai"
# 	for j in options_list[i]:
# 		print j
# 	print ''

line = 0
for i in range (len(question_list)):
	print "Aapka Sawaal hai:-"
	print question_list[i],"\n"
	print "Aapka options hai:-"
	print options_list[i][0]
	print options_list[i][1]
	print options_list[i][2]
	print options_list[i][3]
	user = int(raw_input("input anser "))
	if user == 5050:
		if line != 1:
			line+=1
			print life_line_list[i][0]
			print life_line_list[i][1]
			user = int(raw_input("input anser "))
			if user == solution_list[i]:
				print "aap ka javab sahi hai"
			else:
				print "aap ka javab galat hai aap ki life_line khatam ho gai hai"
		else:
			print "aap already lifeline use kar chuke hai."
			user = int(raw_input("input anser "))
			if user == solution_list[i]:
				print "Congrates aap javab sahi hai"
			else:
				print "Aap ka javab galat hai, try agen"
				print "Aap ko game se bahar kar diya gaya hai."
			print ''



	elif user == solution_list[i]:
		print "Congrates aap javab sahi hai"
	else:
		print "Aap ka javab galat hai, try agen"
		print "Aap ko game se bahar kar diya gaya hai."
		break
	print ''
