from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id : int
    items : List[str] #here list from typing and str from pydantic
    quantities : Dict[str, int]


class BlogPost(BaseModel):
    title : str
    content : str
    image_url : Optional[str] = None #None is a default value

cart_data = {
    "user_id" : 1,
    "items" : ["item1", "item2"],
    "quantities" : {
        "item1" : 2,
        "item2" : 3
    }
}

cart = Cart(**cart_data) # '**' unpacks the dictionary