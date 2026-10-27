# This a base class
class BaseChai:
    def __init__(self, type_):
        self.type = type_


    def prepare(self):
        print(f"Preparing {self.type} chai...")
        
# This is a derived class
""" 
Here the syntax is different as we need give parenthesis in front of class name which will include the base class name.
"""
class MasalaChai(BaseChai):

    def add_spices(self):
        print("Adding cardamom, ginger, clove...")

# -------------------------------------------

# Compositions:
class chaiShop:
    chai_cls = BaseChai # here we are creating a class reference called chai_cls which will be the base class. Here we didn't give parenthesis for class name because we are referencing the class not simply creating an object.

    def __init__(self):
        self.chai = self.chai_cls("Regular") #this is the place where we are actually now creating object

    """ here we are passing the value to chai_cls which is base class and will assign the value type in base class """
    
    def serve(self):
        # now since we have trasnsfered the access to self.chai we can now use it to access the base class properties
        print(f"Serving {self.chai.type} chai...")
        self.chai.prepare()


# let's create another derived class which will inherit the base class from chaiShop

class FancyChaihop(chaiShop):
    chai_cls = MasalaChai


fancy = FancyChaihop()
fancy.serve()   #Even though we server is part of chaishop we can access it as FancyChaihop is inherited from chaiShop

# now let's say I want to access the add_spices method of MasalaChai class

# Then I can't access it directly as we have not inherited it's class but we have created it's reference (chai_cls) in FancyChaihop class

# fancy.chai_cls.add_spices()  --- Commented as it will throw an error

""" but here's the catch, This will throw an error as we are not passing any context to the method and 'add_spices' expects self as first argument.
 """
# In this case we use constructor of inherited class.

fancy.chai.add_spices()



