""" 
set comprehension is more over similar to list.

just instead of [] we will b ehaving {}

"""

favourite_chais = [
    "masala chai",
    "ginger chai",
    "light chai",
    "kadak chai",
    "Peached Ice chai",
    "ginger chai"
]

# example 1: 
unique_chai = {tea for tea in favourite_chais}
print(f"Unique chai types: {unique_chai}")

# exaple 2:
longer_name = {tea for tea in favourite_chais if len(tea) > 12}

print(f"Chai names longer than 12 characters: {longer_name}")


# ---------------------------------------------

# example 3:

recipes = {
    "masala chai": ["masala", "water", "tea leaves"],
    "ginger chai": ["ginger", "water", "tea leaves"],
    "light chai": ["water", "tea leaves"],
    "kadak chai": ["kadak", "water", "tea leaves"],
    "Peached Ice chai": ["peached ice", "water", "tea leaves"],
    "ginger chai": ["ginger", "water", "tea leaves"],
}


unique_spices = { spice for ingrediant in recipes.values() for spice in ingrediant}

print(f"Unique spices: {unique_spices}")

# Here : please note, expression is spice instead of ingrediant -- Beacuse here we write the ultimate goal as expression. In this case ingerediant is just a temporary variable to store values.



