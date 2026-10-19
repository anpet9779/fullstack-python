spice_mix = set()

print(f"The spice mix id is initially: {id(spice_mix)}")
print(f"The spice mix  initially: {spice_mix}")

spice_mix.add("cumin")
spice_mix.add("clove")

print(f"The spice mix id is After: {id(spice_mix)}")
print(f"The spice mix after: {spice_mix}")


# In this example, we create a set called `spice_mix` and print its initial ID. We then add two elements to the set: "cumin" and "clove". After adding these elements, we print the ID of the `spice_mix` set again.

# The initial and after ids are same as 'set()' in python are mutable, It is similar as useState where we can set new values in the variable.

# Output:
# The spice mix id is initially: 2723357835776
# The spice mix  initially: set()
# The spice mix id is After: 2723357835776
# The spice mix after: {'cumin', 'clove'}

