'''
Variable Naming: Public and private
for more info: https://www.python.org/dev/peps/pep-0008/


Public attributes or variable: regular_lower_case
private attributes or variables: _single_leading_underscore
private attributes that shouldnot be subclassed: __double_leading_underscore
Magic attributes: __double_underscores__ (dont create magic attributes)

Although, there are name conventions for encapsulation, python
do not enforce privacy and trust the use to respect it. All private
variables or attributes can be accessed outside class even the one that
is itended not to be subclassed.
'''

class MyClass:
    a = 0 # public attribute
    _b = 1 # private attribute
    __c = 2 # private attribute that shouldn't be subclassed

# python don't enforce privacy. All can be accessed outside of class
my_object = MyClass()
print(my_object.a)
print(my_object._b)
print(my_object._MyClass__c)
