import random

class MyClass(object):
    def generateRandom(self):
        self.randomValue = random.randint(1, 10)

myObject = MyClass()
myObject.generateRandom()
print(myObject.randomValue)
