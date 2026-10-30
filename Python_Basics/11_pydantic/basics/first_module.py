from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str
    is_active : bool

input_data = {'id' : 1, 'name' : 'Amit', 'is_active' : True}

user = User(**input_data) # '**' unpacks the dictionary

print(user)

""" 
The flow is :
1. import BaseModel from pydantic
2. Type Annotation
3. Model Init (Always unpack dictionary with '**')
4. Automatic validation

If we write any number as string instead of str then pydantic convert it in background to Int

for example instead of id=1 we write id="1" and it still works

"""