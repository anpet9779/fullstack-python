# nonlocal keyword is used to access a variable in the parent scope of a function
# nonlocal keyword can be used to modify a variable in the parent scope of a function

def update_order():
    chai_type = "ginger"
    def kitchen():
        nonlocal chai_type  
        chai_type = "masala"

    kitchen()
    print(f"Order for chai: {chai_type}")

update_order()

# output : Order for chai : masala

# if comment ' nonlocal chai_type line no 7' then output will be : Order for chai : ginger


# ------------------------------------------------------------

# Global scope

chai_type = "ginger"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "masala"

    kitchen()
    print(f"Order for chai: {chai_type}")

front_desk()

# output : Order for chai : masala because chai_type is a global variable and it is modified in the kitchen function using global keyword

##  be extra extra carefull while using global keyword and avoid using it if possible




