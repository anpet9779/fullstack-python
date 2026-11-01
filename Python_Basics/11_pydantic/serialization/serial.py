from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []     


    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S"),
        }
    )

user = User(
    id=1,
    name="John Doe",
    email="BhTtK@example.com",
    is_active=True, 
    created_at=datetime.now(),
    address=Address(
        street="123 Main St",
        city="Anytown",
        state="CA",
        zip_code="12345"
    ),
    tags=["tag1", "tag2"]
)

print("User Model:", user)
print("-"*30)
python_dict = user.model_dump()
print("Python Dictionary:", python_dict)


json_string = user.model_dump_json()
print("-"*30)
print("JSON String:", json_string)


 