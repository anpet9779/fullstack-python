from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street : str
    city : str
    postal_code : Optional[str] = None

class User(BaseModel):
    id : int
    name : str
    addresses : Address


address = Address(street="123 Main St", city="New York", postal_code="10001")
user = User(id=1, name="John Doe", addresses=address)

user_data = {
    "id": 2,
    "name": "Jane Smith",
    "addresses": {
        "street": "456 Elm St",
        "city": "Los Angeles",
        "postal_code": "90001"
    }
}

user2 = User(**user_data)