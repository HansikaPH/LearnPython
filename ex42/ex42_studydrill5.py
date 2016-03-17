Demonstrating has-many relationship

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass #pass keyword simply executes nothing.

## Dog is-a Animal.
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name.
        self.name = name

## Cat is-a Animal.
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name.
        self.name = name

## Person is-a object.
class Person(object):

    def __init__(self, name):
        ## Person has-a name.
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None #set to default value none

## Employee is-a Person.
class Employee(Person):

    def __init__(self, name, salary, vehicles):
        ## Calls the __init__ method of the superclass from which Employee inherits.
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary
        ## Employee has-many vehicles
        self.vehicles = vehicles

## Fish is-a object.
class Fish(object):
    pass

## Salmon is-a Fish.
class Salmon(Fish):
    pass

## Halibut is-a Fish.
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is a Person
mary = Person("Mary")

## mary has-a pet named satan
mary.pet = satan

## frank is-a Employee and has-a salary of 120000 and has-many vehicles
frank = Employee("Frank", 120000, ['car', 'van', 'bicycle'])

## frank has-a pet named rover
frank.pet = rover

## flipper is-a Fish.
flipper = Fish()

## crouse is-a Salmon.
crouse = Salmon()

## harry is-a Halibut.
harry = Halibut()
