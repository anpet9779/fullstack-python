def indian_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Match"
    yield "Oolong"


def full_menu():
    yield from indian_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

# ---------------------------

# close:

def chai_stall():

    try:
        while True:
            order=yield "waiting for chai order"
    except:
        print("Chai stall is closed")


stall = chai_stall()
next(stall)
stall.close() #cleanup -- It is good idea to always gracefully close the generator

