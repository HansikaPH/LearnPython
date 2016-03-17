#inheritance vs composition

#implicit inheritance
class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    pass #there's nothing new to define in class Child. Instead it inherits all of its behavior from Parent.

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
