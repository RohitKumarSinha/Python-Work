# animal is-a object (yes, sort of confusing) look at the extra credit

class animal(object):
    pass

# Dog is-a object
class Dog(animal):

    def __init__(self, name):
        # dog has-a __init__ method
        self.name = name

# cat is-a object has-a inherit animal
class Cat(animal):

    def __init__(self, name):
        # cat has-a __init__ method
        self.name = name

# person is-a object
class person(object):

    def __init__(self, name):
        # person has-a __init__ method
        self.name = name

        # person has-a pet of some kind
        self.pet = None

# Employee is-a object
class Employee(person):

    def __init__(self, name, salary):

        # Employee has-a inherit parent name
        super(Employee, self).__init__(name)

        # Employee has-a salary variable
        self.salary = salary

# fish is-a object
class fish(object)::
    pass

# salmon is-a object
class salmon(fish):
    pass

# Halibut is-a object
class Halibut(fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("satan")

# mary is-a person
mary = person('mary')

# mary has-a pet satan
mary.pet = satan

# frank is-a Employee has-a salary 12000
frank = Employee("frank", 12000)

# frank has-a pet named Rover
frank.pet = rover

# flipper is-a fish
flipper = fish()

# crouse is-a salmon
crouse = salmon()

# harry is-a Halibut
harry = Halibut()

 
