def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "peached"]:
        raise ValueError(f"Invalid chai flavor: {flavor}")
    print(f"Brewing {flavor} chai...")

brew_chai("mint")

# raise keyword is used to raise an error