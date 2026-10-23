#  dunder methods
# __docs__

def print_order(name, chai_type):
    """
    Prints the order details.
    :param name: The name of the customer.
    :param chai_type: The type of chai ordered.

    :return: None
    
    """
    print(f"{name} ordered {chai_type} chai.")

print(print_order.__doc__)

# Output:
# Prints the order details.

# __name__

print(print_order.__name__)

# Output:    
# print_order

# ------------------------------------------------  

