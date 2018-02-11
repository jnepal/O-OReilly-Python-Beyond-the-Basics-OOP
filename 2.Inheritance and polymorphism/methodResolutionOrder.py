'''
When multiple class are inherited. Example D inherits B And C, C interherits B
and B inherits A. Python will look in Depth First Search Order

If method is invoked on instance of D. python will look for
method implementation first in C, if it doesn't find it will
look then inorder B, A , C
'''

class A():
    pass

class B(A):
    pass

class C():
    pass

class D(B, C):
    pass


print(D.mro())
