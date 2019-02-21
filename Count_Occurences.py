char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
new_list = []
for i in char_list:
	if i not in new_list:
		new_list.append(i)

a = 0
n = 0
t = 0
x = 0
u = 0
g = 0
for j in char_list:
	if j == "g":
		g+=1
	elif j == "n":
		n=n+1
	elif j == "t":
		t+=1
	elif j == "x":
		x+=1
	elif j == "u":
		u+=1
	elif j == "a":
		a+=1

a_l = []
n_l = []
t_l = []
x_l = []
u_l = []
g_l = []
all_list = []

a_l.append("a")
n_l.append("n")
t_l.append("t")
x_l.append("x")
u_l.append("u")
g_l.append("g")

a_l.append(a)
n_l.append(n)
t_l.append(t)
x_l.append(x)
u_l.append(u)
g_l.append(g)

all_list.append(a_l)
all_list.append(n_l)
all_list.append(t_l)
all_list.append(x_l)
all_list.append(u_l)
all_list.append(g_l)

print all_list
print "a - ",a, "time"
print "n - ",n, "time"
print "t - ",t, "time"
print "x - ",x, "time"
print "u - ",u, "time"
print "g - ",g, "time"



