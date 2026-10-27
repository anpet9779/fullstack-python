chai_menu = {"ginger chai": 20, "black chai": 25, "green chai": 30, "masala chai": 35}


# try:
#     chai_menu["elaichi"]
# except KeyError:
#     print("Elaichi chai is not available")

# print("hello chai")

# --------------------------------------

def server_chai(flavour):
    try:
        print(f"Preparing {flavour} chai...")
        if flavour == "Unknown":
            raise ValueError("Unknown chai type")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavour} chai is ready to serve!")
    finally:
        print("Chai stall is closed")

server_chai("ginger")
server_chai("Unknown")