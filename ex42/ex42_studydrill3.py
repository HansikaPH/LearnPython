#making the classes do things using functions

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def eat(self):
    	print "The animal is eating"
    

## Dog is-a Animal.
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name.
        self.name = name
        
    def eat(self):
    	print "%s, the dog is eating" % self.name    

## Cat is-a Animal.
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name.
        self.name = name
        
    def eat(self):
    	print "%s, the cat is eating" %self.name

## Person is-a object.
class Person(object):

    def __init__(self, name):
        ## Person has-a name.
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None #set to default value none
        
    def work(self):
    	print "%s is working" %self.name

## Employee is-a Person.
class Employee(Person):

    def __init__(self, name, salary):
        ## Calls the __init__ method of the superclass from which Employee inherits.
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary
        
    def work(self, company):
    	print "%s is working at %s" % (self.name, company)

## Fish is-a object.
class Fish(object):
    pass

## Salmon is-a Fish.
class Salmon(Fish):
    pass

## Halibut is-a Fish.
class Halibut(Fish):
    pass

animal = Animal()
animal.eat()

## rover is-a Dog
rover = Dog("Rover")
rover.eat()

## satan is-a Cat
satan = Cat("Satan")
satan.eat();

## mary is a Person
mary = Person("Mary")
mary.work()

## mary has-a pet named satan
mary.pet = satan

## frank is-a Employee and has-a salary of 120000
frank = Employee("Frank", 120000)


## frank has-a pet named rover
frank.pet = rover

frank.work("ABC Company")

## flipper is-a Fish.
flipper = Fish()

## crouse is-a Salmon.
crouse = Salmon()

## harry is-a Halibut.
harry = Halibut()
