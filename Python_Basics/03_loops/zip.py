names = ["Alice", "Bob", "Charlie"]
bills = [25, 30, 15]

# Using zip to iterate over names and bills simultaneously
for name, bill in zip(names, bills):
    print(f"{name} has a bill of ${bill}.")

# Output:
# Alice has a bill of $25.
# Bob has a bill of $30.
# Charlie has a bill of $15.

