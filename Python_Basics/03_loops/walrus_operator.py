""" 
Walrus Operator

The walrus operator is a new assignment expression introduced in Python 3.8. It allows you to assign a value to a variable in a single line of code.    


Syntax:

variable_name := expression


"""

# Example 1: Using walrus operator

value = 13
reminder = value % 5

if reminder:
    print(f"The reminder is: {reminder}")

# Output: The reminder is: 3


# Example 2: Using walrus operator

value = 13
if reminder := value % 5:
    print(f"The reminder is: {reminder}")


# --------------------------------------

#example 3 : 

available_sizes = ["small", "medium", "large"]

if(request_size := input("Enter your preffered cup size? Choose (small | medium | large) :").lower()) in available_sizes:
    print(f"You have selected a {request_size} cup.")
else:
    print("Invalid cup size selected. Please choose from small, medium, or large.")
