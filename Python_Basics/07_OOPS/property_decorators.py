class TeaLeaf:
    def __init__(self, age):
        self._age = age  #'_age has a special meaning in python that it can't be directly modified'

    @property #also known as getter
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self, age):
        if 1<=age<=5:
            self._age = age
        else:
            raise ValueError("Age must be between 1 and 5")


leaf = TeaLeaf(3)
print(leaf.age)

leaf.age = 6
print(leaf.age)
