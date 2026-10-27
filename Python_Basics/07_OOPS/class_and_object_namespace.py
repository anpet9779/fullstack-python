# ----------------------------------------------

# Object Namespace


class Chai:
    origin = "India" #this variable is called as class property

print(Chai.origin) #India

Chai.is_hot = True # adding class property
print(Chai.is_hot) #True

# ---------------------------------------
# Creating object from class Chai

masala = Chai()
print(masala.origin) #India
print(f"Is masala hot? {masala.is_hot}") #masala.is_hot) #True

# ---------------------------------------
# Overriding class property

masala.is_hot = False
print(f"Overridden masala value: {masala.is_hot}") 


