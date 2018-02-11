class MyClass(object):
    a = 5 # public
    '''
        self is the object of the class which
        calls this function.
        
        print(self) and print(myFirstObject) will have
        same hex code if myFirstObject calls this method
    '''
    def sayHello(self):
        print(self)
        print('Hello')


myFirstObject = MyClass()
mySecondObject = MyClass()

'''
     __main__ is namespace
    MyClass is classname
    hexcode is the memory address
'''
print(myFirstObject)
print(mySecondObject)

'''
    Accessing public varible defined inside class
'''
print(myFirstObject.a)

'''
    Accessing methods on class
'''
myFirstObject.sayHello() # passes myFirstObject as the 1st argument

