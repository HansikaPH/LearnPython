#getting input data
#how the ' character in height is escaped when %r is used

print "How old are you?",
age = raw_input() #takes input as string
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight) #' character printed out with raw escape sequences 

print "So, you're %r old, %s tall and %r heavy." % (
    age, height, weight) #' character printed out by using escape sequences 
