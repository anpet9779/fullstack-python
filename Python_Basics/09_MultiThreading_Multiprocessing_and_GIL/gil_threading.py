import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} is brewing chai")

    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing chai")

t1 = threading.Thread(target=brew_chai, name="Chai Maker 1")
t2 = threading.Thread(target=brew_chai, name="Chai Maker 2")

start = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Time taken: {end - start:.2f} seconds")






