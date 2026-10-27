class InvalidChaiError(Exception):pass

def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 25, "peached": 30}
    try:
        if flavor not in menu:
            raise InvalidChaiError(f"Invalid chai flavor: {flavor}")
        
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")
        
        total = menu[flavor] * cups
        print(f"Total Bill : {total}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Thank you for visiting!")

bill("mint", 2)
bill("ginger", "three")
bill("peached", 3)