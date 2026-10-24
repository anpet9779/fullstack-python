cup_size = input("Enter your preffered cup size? Choose (small | medium | large) :").lower()

def calculate_bill(cup_size):
    match cup_size:
        case "small":
            return 10
        case "medium":
            return 15
        case "large":
            return 20
        case _:
            return 0

bill_amount = calculate_bill(cup_size)
print(f"The bill amount is: {bill_amount}")