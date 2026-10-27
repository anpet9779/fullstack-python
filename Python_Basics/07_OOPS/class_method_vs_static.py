class ChaiOrder:
    def __init__(self, tea_type, size, sweetness):
        self.tea_type = tea_type 
        self.size = size
        self.sweetness = sweetness

    @classmethod
    def from_dict(cls, order_data): # this is a class method and 'cls' is reference to class. It's a convention keyword

        return cls(order_data['type'], order_data['size'], order_data['sweetness'])

    @classmethod
    def from_string(cls, order_string):
        tea_type, size, sweetness = order_string.split(',')
        return cls(tea_type, size, sweetness)

class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in [150, 200, 250]

order1 = ChaiOrder.from_dict({'type': 'ginger chai', 'size': 200, 'sweetness': 'less'})
print(order1.__dict__)

order2 = ChaiOrder.from_string('Masala chai,200,less')
print(order2.__dict__)

order3 = ChaiOrder('lemon chai', 200, 'less')
print(order3.__dict__)

