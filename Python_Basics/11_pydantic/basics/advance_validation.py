from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

class Person(BaseModel):
    first_name: str
    last_name: str

    @field_validator("first_name", 'last_name')
    def validate_name(cls, value):
        if not value.istitle():
            raise ValueError("Name must start with a capital letter.")
        return value

class User(BaseModel):
    email :str
    @field_validator("email")
    def normalize_email(cls, v):
        return v.lower().strip()

class Product(BaseModel):
    price : str # $4.44
    
    @field_validator("price", mode='before')
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace("$", ""))
        return v

class dateRange(BaseModel):
    start_date : datetime
    end_date : datetime

    @model_validator(mode='after')
    def validate_date_range(cls, values):
        if values['start_date'] >= values['end_date']:
            raise ValueError("Start date must be before end date.")
        return values