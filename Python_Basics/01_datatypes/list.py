# List

# major difference between list and tuple is that list is mutable and tuple is immutable. Tuple once defined cannot be changed thoughout life cycle, but list can be changed.

ingredients = ["flour", "sugar", "eggs", "milk", "butter"]

ingredients.append("vanilla") # Adding an element to the list

print(f"The ingredients are: {ingredients}")

# Output: The ingredients are: ['flour', 'sugar', 'eggs', 'milk', 'butter', 'vanilla']

# -----------------------------------------------------------


# Removing an element from the list

ingredients.remove("eggs")

print(f"The ingredients are: {ingredients}")

# Output: The ingredients are: ['flour', 'sugar', 'milk', 'butter', 'vanilla']

# -----------------------------------------------------------

# extending a list with another list
extended_ingredients = ["chocolate", "vanilla"]

ingredients.extend(extended_ingredients)

print(f"The ingredients are: {ingredients}")

# extended list gets added to the end of the original list.
# ----------------------------------------------------------

# Insert vs append

# append adds an element to the end of the list
# insert adds an element at a specific index


ingredients.insert(2, "chocolate") # Inserting an element at a specific index

print(f"The ingredients are: {ingredients}")

# Output: The ingredients are: ['flour', 'sugar', 'chocolate', 'milk', 'butter', 'vanilla']

# ----------------------------------------------------------

# pop removes an element from the list

last_added = ingredients.pop(2) # Removing an element at a specific index

print(f"The ingredients are: {ingredients}")

print(f"The last added element is: {last_added}")

# Output: The ingredients are: ['flour', 'sugar', 'milk', 'butter', 'vanilla']
# The last added element is: chocolate

# ------------------------------------------------
ingredients.reverse() # Reversing a list
print(f"The ingredients are: {ingredients}")

# Output: The ingredients are: ['vanilla', 'butter', 'milk', 'sugar', 'flour']

# ------------------------------------------------

sugar_levels  = [5, 10, 15, 20, 25]

sugar_levels.sort() # Sorting a list
print(f"The sugar levels are: {sugar_levels}")
print(f"The max sugar level is: {max(sugar_levels)}")
print(f"The min sugar level is: {min(sugar_levels)}")

# Output: The sugar levels are: [5, 10, 15, 20, 25]
# The max sugar level is: 25
# The min sugar level is: 5

# ------------------------------------------------

# operator overloading in list and bytearray

base_liquids = ["water", "milk"]
extra_flavor = ["vanilla", "chocolate"]

all_liquids = base_liquids + extra_flavor

# like append / extend, + operator can be used to combine two lists. major difference is that append / extend modifies the original list, but + operator creates a new list.

print(f"All liquids: {all_liquids}")

# Output: All liquids: ['water', 'milk', 'vanilla', 'chocolate']

# ------------------------------------------------

strong_brew = ["espresso", "americano"] * 3

print(f"Strong brew: {strong_brew}")
# Output: Strong brew: ['espresso', 'americano', 'espresso', 'americano', 'espresso', 'americano']


# ------------------------------------------------

#bytearray is a mutable sequence of bytes. It is similar to a list of integers in the range 0 <= x < 256. It can be used to manipulate binary data.

# Let's say we have a string "CINNAMON" and we want to create a list out of it 

raw_spices_data = bytearray(b"CINNAMON")
print(f"Raw spices data: {raw_spices_data}")

raw_spices_data = raw_spices_data.replace(b"CINNA", b"CARD")

print(f"Raw spices data: {raw_spices_data}")


