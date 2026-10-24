# Using enumerate to print the menu with index numbers

menu = ["Green Tea", "Black Tea", "Herbal Tea", "White Tea"]

for index, tea in enumerate(menu, start=1):
    print(f"{index}. {tea}")

# Output:
# 1. Green Tea
# 2. Black Tea
# 3. Herbal Tea
# 4. White Tea