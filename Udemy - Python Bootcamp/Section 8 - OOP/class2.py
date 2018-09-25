class Dog():
    # CLASS OBJECT ATTRIBUTE
    species = 'mammal'

    # __init__ é o construtor da classe
    def __init__(self, breed, name):
        # self.breed é um atributo da classe gerada pelo construtor
        self.breed = breed
        self.name = name

    # Operations/Actions ---> Methods
    def bark(self, number):
        print("WOOF! My name is {} and the number is {}".format(self.name, number))

#

mydog = Dog('Lab', 'Frankie')
mydog.bark(2)
#-----------------
class Circle():
    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius*radius*Circle.pi

    # METHOD
    def get_circumfrence(self):
        return self.radius * Circle.pi * 2

mycircle= Circle(30)
mycircle.get_circumfrence()
mycircle.area
#-------------------
class Animal():
    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")
