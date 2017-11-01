# Letterboard string counter for Jess
# this programm accepts a string as user input and returns the number of times each letter occurs

quote = input('Please enter a phrase ')
d = dict()

for x in quote:
	if x =='': continue
	d [x] = d.get(x,0)+1

for let in d:
	print(let, d [let])

