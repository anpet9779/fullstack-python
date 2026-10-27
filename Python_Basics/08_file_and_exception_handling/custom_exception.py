class OutOfStockError (Exception):
    pass


def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfStockError("Out of stock")
    print("Making chai")

make_chai(1,0)