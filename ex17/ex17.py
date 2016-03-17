#copying the content of one file to another.

from sys import argv
from os.path import exists #returns true if a file exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata) #Gets the length of the string that you pass to it then returns that as a number. Play with it.

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
