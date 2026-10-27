def process_order(item, quantity):
    try:
        price = {"masala":20}[item]
        cost = price * quantity
        print(f"total cost is: {cost} " )
    except KeyError:
        print(f"{item} chai is not available")
        
    except TypeError:
        print("Quantity must be a number")

process_order("ginger",2)
process_order("masala",2)
