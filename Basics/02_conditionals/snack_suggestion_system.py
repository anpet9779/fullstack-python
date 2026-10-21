snack = input("Enter your preffered snack:").lower()

print(f"User selected snack: {snack}")

if snack == "cookie" or snack == "samosa":
    print("You can have your snack now.")
else:
    print("Sorry, we don't have that snack available.")

