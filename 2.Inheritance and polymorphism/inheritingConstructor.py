import random

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.breed = random.choice(['Shih Tzu', 'Beagle', 'Mutt'])

    def fetch(self, thing):
        print("%s goes after the %s!" %(self.name, thing))

dog = Dog('Rover')

print(dog.name)
print(dog.breed)
