import threading

counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100_000):
        with lock:
            counter += 1

threads = [ threading.Thread(target=increment_counter) for _ in range(10)]

[t.start() for t in threads]
[t.join() for t in threads]

print(f"final counter value: {counter}")


# lock is used to prevent race conditions - it is used to prevent multiple threads from accessing the same resource at the same time