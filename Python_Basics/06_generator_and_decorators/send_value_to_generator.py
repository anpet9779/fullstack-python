def chai_customer():
    print(f"welcome ! Please give order")
    order = yield #wait for the order
    while True:
        print(f"Your {order} is preparing ")
        order = yield # waiting for the next order if this line is not written then the generator will be infinite loop

stall = chai_customer()
next(stall) # start the generator

stall.send("masala chai")
stall.send("Lemon chai")

