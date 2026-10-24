total_tea_bags = 10
bag_per_cup = 3

total_cups = total_tea_bags / bag_per_cup

print(f"Total cups of tea: {total_cups}")

# / -> Get results in decimal values like 3.3333333333333335

# ------------------------------------------------------------------


total_tea_bags = 10
bag_per_cup = 3

total_cups = total_tea_bags // bag_per_cup

print(f"Total cups of tea: {total_cups}")

# // -> Get results in integer values like 3

# ------------------------------------------------------------------


total_tea_bags = 10
bag_per_cup = 3

remaining_tea_bags = total_tea_bags % bag_per_cup

print(f"Remaining tea bags: {remaining_tea_bags}")

# % -> Get the remainder of the division like 1

# ------------------------------------------------------------------


## '*'  is used for multiplication but '**' is used for exponentiation


total_tea_bags = 10
bag_per_cup = 3

total_cups = total_tea_bags ** bag_per_cup

print(f"Total cups of tea: {total_cups}")

# ** -> Get results in integer values like 10 * 10 * 10 = 1000. i.e 10 to the power of 3.


# ------------------------------------------------------------------


# Python let's us write large number using '_' as a separator for better readability. for example 1_000_000 is same as 1000000. It is just for better readability of the code.

total_tea_leaves = 1_000_000

print(f"Total tea leaves: {total_tea_leaves}")

# Output:
# Total tea leaves: 1000000