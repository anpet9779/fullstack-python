#  dictionary

chai_order = dict(type="masala chai", size="medium", sugar="less", milk="full cream")

print(f"The chai order is: {chai_order}")

# -------------------------------------------------

# Adding new key-value pairs to the dictionary

chai_recipe = {} #empty dictionary

chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "water"

print(f"The chai recipe is: {chai_recipe}")


# -------------------------------------------------
# deleting key-value pairs from the dictionary
del chai_recipe["liquid"]
print(f"The chai recipe is: {chai_recipe}")


# -------------------------------------------------
# updating key-value pairs in the dictionary

chai_recipe["base"] = "green tea"
print(f"The chai recipe is: {chai_recipe}")

# membership test
print(f"'base' in chai_recipe: {'base' in chai_recipe}") # True

# -------------------------------------------------
# Iterating over a dictionary

for key, value in chai_order.items():
    print(f"keys in chai_order: {key}, values in chai_order: {value}")

    # or

print(f"Order details (keys): {chai_order.keys()}")
print(f"Order details (values): {chai_order.values()}")
print(f"Order details (items): {chai_order.items()}") #prints all key-value pairs in the dictionary in the form of tuples
    

last_item = chai_order.popitem() #removes the last item from the dictionary and returns it as a tuple
print(f"Last item removed from chai_order: {last_item}")

# -------------------------------------------------

# updating a dictionary with another dictionary

chai_order.update(chai_recipe)
print(f"The chai order is: {chai_order}")

# -------------------------------------------------

customer_note = chai_order.get("customer_note", "No note")

print(f"Customer note: {customer_note}") # prints "No note" since the key "customer_note" does not exist in the dictionary