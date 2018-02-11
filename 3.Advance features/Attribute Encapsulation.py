'''
   @property shouldnot encapsulate expensive operations,
    because attribute setting looks cheap
'''

class GetSet:

    @property
    def var(self):
        print('Getting the "var" attribute')
        return self.attrval

    @var.setter
    def var(self, value):
        print('Setting the "var" attribute')
        self.attrval = value

    @var.deleter
    def var(self):
        print('Deleting the "var" attribute')
        self.attrval = None


a = GetSet()

a.var = 100
print(a.var)
del(a.var)
print(a.var)