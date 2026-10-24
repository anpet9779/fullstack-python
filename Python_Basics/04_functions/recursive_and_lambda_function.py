def pour_chai(n):
    print(f"Pouring chai {n}")
    if n == 0:
        return "All cups poured"
    return pour_chai(n-1)

print(pour_chai(3))


# -------------------------------------------

""" Lambda functions are anonymous functions """

chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai == "kadak", chai_types))

print(strong_chai)

""" 

Output : ['kadak', 'kadak']

explaination : 

lambda chai: chai == "kadak" is a lambda function that takes chai as an argument and returns True if chai is equal to "kadak".

lamda is used when we want to create a function that is only used once.

"""