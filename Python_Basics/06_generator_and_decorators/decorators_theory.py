# Decorators are used as wrappers whcih can have common functionality added to a function which which can be then used into any sub function or extensions 
from functools import wraps  #to get metadata

def my_decorator(func):
    @wraps(func) #to get metadata
    def wrapper():  #keyword wrapper
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


#which ever function you want to send in warpper should be written under the decorator where decorator starts with '@' followed by the name of the decorator
@my_decorator   
def say_whee():
    print("Whee!")

say_whee()


""" 
Output:

Something is happening before the function is called.
Whee!
Something is happening after the function is called.
"""

# but if we simply try to get meta data it will return wrapper instead of say_whee

print(say_whee.__name__)
# Output: wrapper

""" 
to get the name of the original function we can import wraps from functools 

"""

print(say_whee.__name__)
# Output: say_whee

# -------------------------------------------

