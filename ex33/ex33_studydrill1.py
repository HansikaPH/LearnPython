#while loop converted to a function

numbers = []
limit = 6

def whileloop(i):
	if i<limit:
		print "At the top i is %d" % i
       	numbers.append(i)

    	i = i + 1
    	print "Numbers now: ", numbers
    	print "At the bottom i is %d" % i
    	whileloop(i)

whileloop(0)
		

print "The numbers: "

for num in numbers:
    print num
