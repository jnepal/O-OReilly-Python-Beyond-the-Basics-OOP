class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, thing):
        print("%s is eating %s" %(self.name, thing))

class Dog(Animal):
    def fetch(self, thing):
        print("%s goes after the %s" %(self.name, thing))

class Cat(Animal):
    def swatString(self):
        print("%s shreds the string" %(self.name))

dog = Dog('Rover')
cat = Cat('Fluffy')

dog.fetch('paper')
cat.swatString()
dog.eat('dog food')
cat.eat('cat food')