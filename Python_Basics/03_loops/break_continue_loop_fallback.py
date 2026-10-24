flavours = ["Vanilla", "Chocolate", "Strawberry", "Mango", "Pista"]

for flavour in flavours:
    if flavour == "Strawberry":
        print(f"{flavour} is not available. Skipping this flavour.")
        continue
    print(f"Preparing {flavour} ice cream...")

    if flavour == "Mango":
        print(f"{flavour} is the last flavour to prepare. Stopping the preparation.")
        break
    print(f"{flavour} ice cream is ready to serve!")


    # Output:
""" 
Preparing Vanilla ice cream...
Vanilla ice cream is ready to serve!

Preparing Chocolate ice cream...
Chocolate ice cream is ready to serve!

---- Continue hits here ----
Strawberry is not available. Skipping this flavour.
Preparing Mango ice cream...

---- Break hits here -----
Mango is the last flavour to prepare. Stopping the 
preparation. 

Pista never got chance to print as loop breaks on Mango.



###
Continue --> Skips the item in loop
break --> ends the loop on encontering particular item
###
"""