""" 
dictionary is same as set comprehension only change comes in for expression -- which is ultimate goal is considered as expression

"""


tea_prices = {
    "masala chai": 20,
    "ginger chai": 40,
    "light chai": 10,
    "kadak chai": 50,
    
}

# convert INR to USD by dividing by 80

inr_to_usd = {tea:price/80 for tea, price in tea_prices.items()}

# here division of prices by 80 is expression
# any computation can be done and considered in expression 

print(f"prices in USD : {inr_to_usd}")
