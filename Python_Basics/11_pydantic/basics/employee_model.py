from typing import Optional
from pydantic import BaseModel, Field

class Employee(BaseModel):
    id : int
    name : str = Field(
        ..., #'...' means required
        min_length = 1,
        max_length = 50,
        description="Name of the employee",
        examples = "Parag"
    )   
    age : Optional[int]
    salary : float = Field(
        ...,
        gt = 1000
    )


    

