sugar_amount = 2
print(f"The amount of sugar is {sugar_amount} teaspoons.")

sugar_amount = 12

print(f"The amount of sugar is {sugar_amount} teaspoons.")

print(f"ID of 2: {id(2)}")  #140728564933936
print(f"ID of 12: {id(12)}") #140728564934256


# Numbers are immutable, so when we change the value of sugar_amount, we are actually creating a new integer object and assigning it to the variable sugar_amount. The old integer object (2) still exists in memory, but it is no longer referenced by sugar_amount.

# When we print the ID of 2 and 12, we see that they are different.

# In summary, numbers are immutable in Python, so when we change the value of a number, we are actually creating a new object and assigning it to the variable. -- It is changing the reference of the variable to a new object, not modifying the original object.