import yaml

my_dict = {'a': 1, 'b': 2, 'c': 3}
my_list = [1, 2, 3, 4, 5]
my_tuple = ('x', 'y', 'z')

loaded_yaml = yaml.dump(my_dict)

print(loaded_yaml)

print(yaml.dump(my_list))
print(yaml.dump(my_tuple))

my_obj = (
    [1, 2, 3, 4, 5],
    {'a': 1, 'b': 2, 'c': 3},
    [
        {'x': 98, 'y': 99, 'z': 100},
        3,
        4
    ],
    {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
)

print(yaml.dump(my_obj))

'''
    yaml.load(file_to_load_from) to load yaml file.
    syntax similar to JSON or Pickle
'''

class MyClass:
    def __init__(self, val):
        self.val = val

    def increment(self):
        self.val += 1

a = MyClass(5)
a.increment()
a.increment()

with open('test.yaml', 'w') as file:
    yaml.dump(a, file)

with open('test.yaml', 'r') as file:
    # yaml.safe_load(file) will limit the loading of objects to plain
    # python structures like dictionaries, list and tuples not instances of class
    my_class_object = yaml.load(file)

print(my_class_object.val)