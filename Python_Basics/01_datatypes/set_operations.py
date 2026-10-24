# Sets 

#Union
essential_spices = {'cardamom', 'cinnamon', "ginger"}
optional_spices = {'clove', 'ginger', 'nutmeg'}

all_spices = essential_spices | optional_spices 

print(f"All spices: {all_spices}")

# -------------------------------

# Intersection
common_spices = essential_spices & optional_spices 

print(f"Common spices: {common_spices}")

# -------------------------------

# Difference

only_in_essential_spices = essential_spices - optional_spices 

print(f"Only in essential spices: {only_in_essential_spices}")

# -------------------------------
# membership testing

print(f"Is 'cinnamon' in essential spices? {'cinnamon' in essential_spices}")

# -------------------------------
frozenset_spices = frozenset(essential_spices)
print(frozenset_spices)