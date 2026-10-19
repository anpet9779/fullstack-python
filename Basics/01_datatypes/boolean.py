is_boiling = True
stri_count = 5

total_actions = stri_count + is_boiling #this is known as upcasting. Python automatically converts the boolean value to integer value. True is converted to 1 and False is converted to 0.

print(total_actions) # Output: 6

# ------------------------------------------------------------------


milk_present = 0 #no milk
print(f"Milk present? {bool(milk_present)}") # Output: Milk present? False

# 'bool' function is used to convert a value to a boolean value (True/False).
## only handful of values gets converted to False and '0' and 'None' are one of them. Rest of the other values are converted to True.

#------------------------------------------------------------------

# Logical Operations : 

# and, or, not

