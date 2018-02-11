'''
    with will automatically run cleanup routine
    like with open() as file will close the file handle
'''

class MyClass:
    def __enter__(self):
        print('Entered')
        print(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exited")
        print(self)

    def say_hi(self):
        print('Hi, instance of %s' %(id(self)))

# Without with context
# a = MyClass()
# a.say_hi()

# With with context
with MyClass():
    MyClass().say_hi()

print('After the "with" block')