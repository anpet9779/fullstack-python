# Tuples

masala_spices = ("cumin", "coriander", "turmeric")

(spice1, spice2, spice3) = masala_spices

print(f"The spices are: {spice1}, {spice2}, {spice3}") 

# Output: The spices are: cumin, coriander, turmeric -- Like spreading operator in JS, we can unpack the tuple values into individual variables.

# Tuples are immutable

# Membership test

if "cumin" in masala_spices:
    print("Cumin is present in masala spices")
else:
    print("Cumin is not present in masala spices")

# ---------------------------------------------------
    print(f"Cumin is present in masala spices? { 'cumin' in masala_spices }") # Output: Cumin is present in masala spices? True

# This is case sensitive, so if we check for "Cumin" it will return False.