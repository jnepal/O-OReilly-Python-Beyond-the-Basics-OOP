class InstanceCounter(object):
    count = 0

    def __init__(self, value):
        self.val = value
        InstanceCounter.count += 1

    def set_val(self, newVal):
        self.val = newVal

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count

a = InstanceCounter(5)

print(a.get_val())
print(a.get_count())

b = InstanceCounter(6)
print(a.get_count())