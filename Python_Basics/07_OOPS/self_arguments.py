class Chai:
    size = 150

    def describe(self):
        return f"The chai is {self.size} ml in size."
cup = Chai()
print(cup.describe()) #The chai is 150 ml in size
print(Chai.describe()) #This will throw an error as self is not passed in describe method. Self gives context to the method therefore we need to pass context e.g:

print(Chai.describe(cup))

# Now this will work.

# let's say there's another obj with different context.

cup_two = Chai()
cup_two.size = 200
print(Chai.describe(cup_two))

# Now this will work and will print the size as 200.
