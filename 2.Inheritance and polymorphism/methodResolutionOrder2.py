'''
For Cyclic Diamond Inheritance Resolution like
If D inherits B and C and both B and C inherits A
the method resoultion order will be B, C, A
'''

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())