'''
Every thing in the python is the object. While other languages make use
of primitives but in python everything is object
'''

myNumber = 5

print(type(myNumber))

myString = 'test'

print(type(myNumber))

def myFunction():
    return 'Hello';

print(type(myFunction))

# Even the type() is object
print(type(type))

# Find the methods available to the object
print(dir(myString))

class Hello:
    pass

print(type(Hello)) # Even Class is object
print(dir(Hello)) # finde methods available on class