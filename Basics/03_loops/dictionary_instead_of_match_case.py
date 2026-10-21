users = [
    {
        "name": "Amit",
        "total": 100,
        "coupon" : "P20"
    },
    {
        "name": "Zara",
        "total": 130,
        "coupon" : "F10"
    },
    {
        "name": "Raj",
        "total": 150,
        "coupon" : "P50"
    }
    
]

discounts = {
    "P20": (0.2, 0),
    "F10": (0.1, 10),
    "P50": (0.5, 0)
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
    print(f"User: {user['name']}, Total: {user['total']}, Discount: {discount}")

""" 
Output:

User: Amit, Total: 100, Discount: 20.0 -- 20% discount on 100
User: Zara, Total: 130, Discount: 23.0 -- 10% discount on 130 + 10rs flat discount
User: Raj, Total: 150, Discount: 75.0 -- 50% discount on 150

"""