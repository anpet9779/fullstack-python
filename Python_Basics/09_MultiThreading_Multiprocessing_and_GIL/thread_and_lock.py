import threading
import time

def boil_milk():
    print("Boiling milk...")
    time.sleep(3)
    print("Milk boiled!")

def toast_bun():
    print("Toasting bun...")
    time.sleep(3)
    print("Toasting done!")

start = time.time()

t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Time taken: {end - start:.2f} seconds")


# -------------------------------------------


def prepare_chai(type_, wait_time) :
    print(f"Preparing {type_} chai...")
    time.sleep(wait_time)
    print(f"{type_} chai is ready!")


# passing arguments in thread

t1 = threading.Thread(target=prepare_chai, args=("ginger", 3))
t2 = threading.Thread(target=prepare_chai, args=("black", 5))

start = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Time taken: {end - start:.2f} seconds")
    
