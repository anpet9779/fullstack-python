from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied")
            return None
        else:
            func(user_role)
    return wrapper


@require_admin
def access_inventory(role):
    print("Access granted")

access_inventory("admin")
access_inventory("user")