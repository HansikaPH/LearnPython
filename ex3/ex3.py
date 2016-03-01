#Python follows the PEMDAS order when doing calculations
print "I will now count my chickens:"


#can print several arguments using one print function and a comma between the arguments 
#do the division first(30/6=5) and then perform the addition(25+5=30) 
print "Hens", 25 + 30 / 6

#perform the multiplication first(25*3=75), then the modulus(75%4=3) and finally the subtraction(100-3=97)
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

#(4%2=0) first then, (1/4=0) and finally the addition/subtraction(3 + 2 + 1 - 5 + 0 - 0 + 6 = 7)
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

#compares 5 and -2 and returns true if 5 is smaller than -2 and false otherwise
print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
