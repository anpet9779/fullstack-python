""" 
There are different types of scopes : 
1. Local -- Inside function
2. Enclosing -- Inside enclosing function if nested
3. Global
4. Built-in -- like print

"""

def serve_chai():
    chai_type = "ginger" #local
    print("inside funtion {chai_type}...")

chai_type = "masala"
print("outside function {chai_type}...")

serve_chai()

# ------------------------------------------------

def chai_order():
    chai_type = "ginger"

    def print_order():
        chai_type = "masala"
        print(f"Inner {chai_type} .")
    print_order()
    print(f"Outer {chai_type} .")

chai_type = "masala"
chai_order()
print(f"Global {chai_type} .")

