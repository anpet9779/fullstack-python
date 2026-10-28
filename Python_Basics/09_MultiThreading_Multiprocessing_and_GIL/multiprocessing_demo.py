from multiprocessing import Process
import time


def brew_chai(name):
    print(f"Brewing chai for {name}")
    time.sleep(3)
    print(f"Chai brewed for {name}")


if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai Maker #{i+1}", ))
        for i in range(5)
    ]

    # Start all process
    for p in chai_makers:
        p.start()

    # Wait for all to complete
    for p in chai_makers:
        p.join()

    print("All chai is brewed")