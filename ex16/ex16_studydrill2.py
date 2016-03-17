#reading the created file

from sys import argv

script, filename = argv

txt = open(filename) #open a fie and return a file object

print "Here's your file %r:" % filename
print txt.read()

txt.close()
