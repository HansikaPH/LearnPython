#taking arguments in python script

#add features(modules) to the python script from the python features set(modules set)
#sys is the package where you take the module argv from
from sys import argv #argv is the feature(module). This holds the arguments you pass to the python script at runtime. 

script, first, second, third = argv  #Take whatever is in argv, unpack it, and assign it to all of these variables on the left in order
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
