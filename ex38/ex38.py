#list functions

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ') #Python interpretes this function call as split(ten_things, ' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() #Python interpretes this function call as pop(more_stuff)
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] #returns the last element of the list. useful when you do not know the length of the list.
print stuff.pop() #removes and returns the last element of the list. 
print ' '.join(stuff) #joins the elements in the list into a string with a ' ' in between the elements and return the string.  
print '#'.join(stuff[3:5]) #joins the elements 3 and 4 with a '#' in between and returns the string.(stuff[3:5] works sismilar to range() where it excludes the last element)
print stuff
