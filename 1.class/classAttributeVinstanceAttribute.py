class MyClass:
    classAttribute = 'Class Attribute'
    def myMethod(self):
        self.instanceAttribute = 'Instance Attribute'

myObject = MyClass()
print(myObject.classAttribute)
myObject.myMethod()
print(myObject.instanceAttribute)

'''
    Python first looks the attribute in instance
    and then searches it on class
'''

class MySecondClass:
    attribute = 'Class Attribute'

    def myMethod(self):
        self.attribute = 'Instance Attritbute'

mySecondObject = MySecondClass()
print('-- Second Class--')
print(mySecondObject.attribute)
mySecondObject.myMethod()
print(mySecondObject.attribute)

del(mySecondObject.attribute)
print(mySecondObject.attribute)