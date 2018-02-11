class InstanceCounter:
    count = 0

    def __init__(self, value):
        self.val = value
        InstanceCounter.count += 1

    def set_val(self, newVal):
        self.val = newVal

    def get_val(self):
        return self.val
    '''
        Even thought the method is called on 
        class instance, the class is passed as
        the first parameter
        
        cls stores class
    '''
    @classmethod
    def get_count(cls):
        print(cls)
        return cls.count

a = InstanceCounter(5)
print("Value of a: %s" %(a.get_val()))
print("count: %s" %(a.get_count()))
b = InstanceCounter(13)
print("Value of b: %s" %(b.get_val()))
print("count: %s" %(b.get_count()))
