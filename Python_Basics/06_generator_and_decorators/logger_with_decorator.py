from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper


@log_activity
def chai_brewing(type):
    print(f"{type} chai is brewing")

chai_brewing("Masala")


# Output:

# Starting chai_brewing
# Masala chai is brewing
# Finished chai_brewing