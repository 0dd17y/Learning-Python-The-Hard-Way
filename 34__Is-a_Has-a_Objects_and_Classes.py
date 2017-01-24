## Animal is-a object (Yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

##Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ##name is-a parameter of init
        self.name = name
class Cat(Animal):
    def __init__(self, name):
        ##
        self.name = name

## Person is-a object.
class Person(object):
    def __init__(self, name):
        ##self has an attribute name
        self.name = name

        ##Person has-a pet of some kind
        self.pet = None

##Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ##?? what is this strange magic?
        super(Employee, self).__init__(name)
        ##??
        self.salary = salary

## Fish is-a object
class Fish(Object):
    pass

#Salmon is-a fish
class Salmon(Fish):
    pass

##Halibut is-a fish
class Halibut(Fish):
    pass

##rover is-a dog
rover = Dog("Rover")

##satan is-a cat
satan = Cat("Satan")

#Mary is-a person
mary = Person("Mary")

#Marys pet is satan
mary.pet = satan

##Frank is-a Employee with attributes "Frank" and "120000"
frank = Employee("Frank", 120000)

##Franks pet is-a rover
frank.pet = rover

##Flipper is-a new instance of Fish()
flipper = Fish()

##Crouse is-a instance of Salmon()
crouse = Salmon()

##harry is-a instance of Halibut()
harry = Halibut()











