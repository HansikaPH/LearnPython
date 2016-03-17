#functions in python

#def keyword denotes that it's a function 

# this one is like your scripts with argv
#* in args tells to take all the arguments to the function and then put them in args as a list. 
def print_two(*args): #*args is like argv which holds many values but used with functions.
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."

#calling functions
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
