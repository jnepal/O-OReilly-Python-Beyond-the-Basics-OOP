'''
 + is operator used to concadinate strings,
 add number, append lists. But + is just syntatic
 sugar. What happens under the hood ?

 lets suppose
 var a = 1
 var b = 2
 when we execute a+b , what python does is calls the
 magic method on a
 a.__add__(b)

 Similary other Core Syntax resolutions:

 'abc' in var => var.__contains__('abc')
 var == 'abc' => var.__eq__('abc')
 var[1]       => var.__getitem__(1, 3)
 var[1:3]     => var.__getslice__(1, 3)
 len(var)     => var.__len__()
 print(var)   => var.__repr__()
'''

class SumList:
    def __init__(self, list):
        self.list = list

    def __add__(self, other):
        newList = [ x + y for x, y in zip(self.list, other.list)]

        return SumList(newList)

    def __repr__(self):
        return str(self.list)

a = SumList([1, 2, 3, 4, 5])
b = SumList([100, 200, 300, 400, 500])

print(a + b)