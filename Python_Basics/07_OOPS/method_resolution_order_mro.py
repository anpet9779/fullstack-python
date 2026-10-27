class A:
    label = "A: Base Class"

class B(A):
    label = "B: Derived Class 1"

class C(A):
    label = "C: Derived Class 2"

class D(B, C):
    pass

cup = D()
print(cup.label)

# Output:: Derived Class

# as B is given as first argument so it will be called first. If we change the order then it will be called in reverse order

print(D.__mro__)
# Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
