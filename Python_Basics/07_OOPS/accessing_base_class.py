# There are 3 ways to access base class


# 1. 

class BaseChai:
    def __init__(self, type_, strength):
        self.type_ = type_
        self.strength = strength

""" 
class GingerChai(BaseChai):
    def __init__(self, type, strength, spice_level):
        self.type = type
        self.strength = strength
        self.spice_level = spice_level 

    This is one way of accessing base class
    but it is code duplication. We have already defined properties in base class and now again doing it in derived class.

"""
# Instead we have another way
# 2.

""" 
class GingerChai(BaseChai):
    def __init__(self, type_, strength, spice_level):
        BaseChai.__init__(self, type_, strength)
        self.spice_level = spice_level 

        This can be used but there's another better way
"""

# 3.
class GingerChai(BaseChai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level

# Method 2 add 3 are same only difference is #2 gives explicit reference to base class where as #3 uses super() which is common reference


