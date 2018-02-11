'''
Pickle is python-native object storage.
It can store most Python objects on disk but doesn't
store classes, modules or functions but can refer to them
'''

import pickle

mylist = ['a', 'b', 'c', 'd']

# Saving mylist
with open('datafile.txt', 'wb') as file:
    pickle.dump(mylist, file)

# Getting Content
with open('datafile.txt', 'rb') as file:
    unpickled_list = pickle.load(file)

print(unpickled_list)

'''
    pickling in variable
'''

pickled_list = pickle.dumps(mylist)
print(pickle.loads(pickled_list))

'''
    Saving Instance
'''

class MyClass:
    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value += 1

my_object = MyClass(5)
my_object.increment()
my_object.increment()

with open('datafile.txt', 'wb') as file:
    pickle.dump(my_object, file)

with open('datafile.txt', 'rb') as file:
    unpickled_my_object = pickle.load(file)

print(unpickled_my_object)
print(unpickled_my_object.value)