class Chai :

    temperature = "hot"
    strenghth = "strong"

cutting_chai = Chai()
print(cutting_chai.temperature)

cutting_chai.temperature = "cold"

print(f"After changing the value of temperature: {cutting_chai.temperature}")
print(f"Before changing the value of temperature: {Chai.temperature}")

del cutting_chai.temperature

print(f"After deleting the value of temperature: {cutting_chai.temperature}")  
print(f"Before deleting the value of temperature: {Chai.temperature}") 


#value will be then changed back to default value given in the class -- Because the value of temperature deleted was injected value but actual / default class attribute is still there.

# let's say if we add another attribute using "cutting_chai.cup = 'small'" and then delete it the it will give AttributeError.



