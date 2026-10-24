# args are passed while calling function and params are received in function


""" 
there are two types 
1. args -- Position based args 
2.kwargs -- Keyword based args

"""

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)


make_chai("Assam", "Yes", "Low")  #Positional
make_chai(tea="Assam", sugar="Medium", milk="no")  #keyword based, here postion doesn't matter


""" 
Output
--------
Assam Yes Low
Assam no Medium

"""
 
# ---------------------------------------------

def special_chai(*ingrediants, **extras):
    print(f"Ingrediants : {ingrediants}")
    print(f"Extras : {extras}")

special_chai("Cinnamon", "Cardmom", sweetner="yes", milk="no")


""" 
Output
--------
Ingrediants : ('Cinnamon', 'Cardmom') -- '*' works as args (tuples)
Extras : {'sweetner': 'yes', 'milk': 'no'} -- '**' works as kwargs (dictionary)

"""


""" 
Note: While passing default values in params instead of using [] (empty list) use 'none'  

"""