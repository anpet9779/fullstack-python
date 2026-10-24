cup_size = input("Enter your preffered cup size? Choose (small | medium | large) :").lower()

match cup_size:
    case "small":
        print("You have selected a small cup. The price is $10.")
    case "medium":
        print("You have selected a medium cup. The price is $15.")
    case "large":
        print("You have selected a large cup. The price is $20.")
    case _:
        print("Invalid cup size selected. Please choose from small, medium, or large.")

