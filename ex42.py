## Animal is-a object 
class Animal(object):
    pass

#Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
       # self.name has-a name
       self.name = name

#Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        #self.name has-a name
        self.name = name

#Person is-a object
class Person(object):
    def __init__(self, name):
        #self.name has-a name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

#Employee is a Person
class Employee(Person):
    def __init__(self, name, salary):
        ##Employee has-a name
        super(Employee,self).__init__(name)
        ##self.salary has-a salary
        self.salary = salary

#Fish is-a class
class Fish(object):
    pass

#salmon is-a Fish
class Salmon(Fish):
    pass

#Halibut is-a Fish
class Halibut(Fish):
    pass

##rover is-a Dog
rover = Dog("Rover")

##satan is a Cat
satan = Cat("Satan")

##mary is-a Person
mary = Person("Mary")

##
mary.pet = satan

#frank is-a employee
frank = Employee("Frank", 120000)

#frank has-a pet rover
frank.pet = rover

##
flipper = Fish()

##crouse
crouse = Salmon()

##
harry = Halibut()
