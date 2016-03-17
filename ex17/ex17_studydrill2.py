#copying the content of one file to another.

from sys import argv
from os.path import exists #returns true if a file exists

script, from_file, to_file = argv

open(to_file, 'w').write(open(from_file).read()) #this line automatically closes the opened file objects once the line finishes executing.


