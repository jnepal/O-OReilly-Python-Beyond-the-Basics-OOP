import abc

class GetSetParent:
    __metaclass__ = abc.ABCMeta

    def __init__(self, val):
        self.val = val

    def set_val(self, val):
        self.val = val

    def get_val(self):
        return self.val

    @abc.abstractmethod
    def showdoc(self):
        return

class GetSetInt(GetSetParent):
    def set_val(self, val):
        if not isinstance(val, int):
            val = 0

        super().set_val(val)

    def showdoc(self):
        print("GetSetInt objece ({0}), only accepts integer values".format(id(self)) )


a = GetSetInt(3)
a.set_val(5)
print(a.get_val())
a.showdoc()

class GetSetList(GetSetParent):
    def __init__(self, value = 0):
        self.vallist = [value]

    def get_val(self):
        return self.vallist[-1]

    def get_vals(self):
        return self.vallist

    def set_val(self, val):
        self.vallist.append(val)

    def showdoc(self):
        print("GetSetList object, len {0}, stores history of values set".format(len(self.vallist)))

getSetList = GetSetList(5)
getSetList.set_val(10)
getSetList.set_val(20)
print(getSetList.get_val())
print(getSetList.get_vals())
getSetList.showdoc()
