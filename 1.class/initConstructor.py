class MyNum():
    def __init__(self,value):
        self.value = value #public variable

    def getValue(self):
        return self.value

myObj = MyNum(5)
print(myObj.getValue())

myObj.value = 6
print(myObj.getValue())