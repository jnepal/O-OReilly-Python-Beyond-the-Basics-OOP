class InstanceCounter:
    count = 0

    def __init__(self, val):
        self.val = self.filterInt(val)
        InstanceCounter.count += 1

    '''
        Even though it is called on the instance
        the instance will not be passed as first
        argument
    '''
    @staticmethod
    def filterInt(val):
        if not isinstance(val, int):
            return 0
        else:
            return val

a = InstanceCounter(5)
print(a.val)
b = InstanceCounter(13)
print(b.val)
c = InstanceCounter('hello')
print(c.val)