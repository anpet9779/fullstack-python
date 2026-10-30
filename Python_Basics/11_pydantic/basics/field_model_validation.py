from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str

    @field_validator("username")
    def validate_username(cls, value):
        if len(value) < 3:
            raise ValueError("Username must be at least 3 characters long.")
        return value