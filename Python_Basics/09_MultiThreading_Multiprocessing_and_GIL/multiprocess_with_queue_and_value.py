import threading
import time
from multiprocessing import Process, Queue, Value

# def cpu_heavy():
#     print(f"Crunching some numbers...")
#     total = 0
#     for i in range(10**7):
#         total += i
#     print(f"done and total: {total}")

# start = time.time()
# threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]

# [t.start() for t in threads]
# [t.join() for t in threads]

# end = time.time()

# print(f"Time taken for threading: {end - start:.2f} seconds")

# Output :
# Time taken for threading: 1.9 seconds

# ---------------------------------------------

# def cpu_heavy():
#     print(f"Crunching some numbers...")
#     total = 0
#     for i in range(10**7):
#         total += i
#     print(f"done and total: {total}")

# if __name__ == "__main__" :
#     start = time.time()
#     processes = [Process(target=cpu_heavy) for _ in range(2)]

#     [t.start() for t in processes]
#     [t.join() for t in processes]

#     end = time.time()

#     print(f"Time taken for process: {end - start:.2f} seconds")

# Output :
# Time taken for process: 0.91 seconds

# -------------------------------------------

# With Queue

# def prepare_chai(queue):
#     queue.put("Chai is ready")


# if __name__ == "__main__" :
#     queue = Queue()

#     p = Process(target=prepare_chai, args=(queue, ))

#     p.start()
#     p.join()

#     print(queue.get())


# ------------------------------------------------
# With Value 

def increment(counter):
    for _ in range(100_000):
        with counter.get_lock():
            counter.value += 1


if __name__ == "__main__" :
    counter = Value("i", 0)

    processes = [Process(target=increment, args=(counter, ))for _ in range(4)]

    [p.start() for p in processes ]
    [p.join() for p in processes ]

    print(f"final counter value : {counter.value}")