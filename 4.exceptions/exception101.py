'''
    Handling Exceptions
'''
import sys
mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

key = input('please input a key: ')

try:
    print("The value for {0} is {1}".format(key, mydict[key]))

except KeyError as err:
    print('the key ' + key + ' does not exists')
    print(err)
    # print(sys.exc_info()[0])


'''
    Raising Exceptions
'''

def divideByZero(num):
    return num / 0

try:
    divideByZero(5)
except ZeroDivisionError as error:
    raise ZeroDivisionError("ZeroDivisionError: You cannot divide a number by zero")
