class ChaiOrder:
    def __init__(self, type_, size):
        self.type = type_ # '_' was added because there is already a built-in function called 'type' there to differentiate we added underscore.
        self.size = size

    def summary(self):
        return f"Type: {self.type}, Size: {self.size}"

order = ChaiOrder("masala chai", 200)
print(order.summary())

order_two = ChaiOrder("ginger chai", 150)
print(order_two.summary())



