import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Order {i} taken")
        time.sleep(2)

def brew_chai():
    for i in range(1, 4):
        print(f"Brewwing for {i}")
        time.sleep(3)

# creating threads

t1 = threading.Thread(target=take_orders)
t2 = threading.Thread(target=brew_chai)

# starting threads
t1.start()
t2.start()

# waiting for both threads to finish
t1.join()
t2.join()

print("All orders are ready")