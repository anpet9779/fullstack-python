# [expression for item in iterable if condition]

menu = [
    "masala chai",
    "ginger chai",
    "light chai",
    "kadak chai",
    "Peached Ice chai"
]

# exmaple 1 :
""" 
ginger_tea = [expression for item in iterable if condition]

expression = tea
item = tea
iterable = menu
condition = "ginger" in tea

**expression and item should be named the same

 """

ginger_tea = [tea for tea in menu if "ginger" in tea]
print(f"example 1 output:{ginger_tea}")
# Output : ['ginger chai']

# example 2:
long_name = [tea for tea in menu if len(tea) > 12]
print(f"example 2 output: {long_name}")

# output : ['Peached Ice chai']



