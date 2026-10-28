from multiprocessing import Process
import time


def crunch_number():
    print("started the count...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print("finished the count...")

if __name__ == "__main__" :
    start = time.time()
    p1 = Process(target=crunch_number)
    p2 = Process(target=crunch_number)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()

    print(f"Time taken: {end - start:.2f} seconds")



""" Output:
GIL - Multiprocessing :


started the count...
started the count...
finished the count...
finished the count...
Time taken: 6.07 seconds

----------------------------------------------

GIL - Threading :

Chai Maker 1 is brewing chai
Chai Maker 2 is brewing chai
Chai Maker 2 finished brewing chai
Chai Maker 1 finished brewing chai
Time taken: 9.19 seconds
 
"""