def server_chai():
    yield "masala chai"
    yield "ginger chai"
    yield "light chai"
    yield "kadak chai"
    yield "Peached Ice chai"

stall = server_chai()

for chai in stall:
    print(chai)

def get_chai_list():
    return ["cup 1", "cup 2", "cup 3", "cup 4", "cup 5"]

# generator function 

def get_chai_list():
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"
    yield "cup 4"
    yield "cup 5"

chai = get_chai_list()
print(next(chai))

# next function is used to get next value from the generator similar to for loop
