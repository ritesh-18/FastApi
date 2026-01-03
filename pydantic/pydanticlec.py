# here we will talk about pydantic and its use cases
# Pydantic is a data validation + parsing library for Python that is built on type hints.
'''
You define how data should look
Pydantic checks, converts, and guarantees correctness
If data is invalid → it throws structured errors

Why Pydantic was needed (Problem it solves)
  - Before Pydantic, Python had:
  - No runtime type safety
  - Manual if/else validation everywhere
  - Unclear error messages
  - No standard data contracts

Pydantic gives you 4 superpowers:

| Feature        | What it means                   |
| -------------- | ------------------------------- |
| Validation     | Checks incoming data            |
| Parsing        | Converts types automatically    |
| Serialization  | Converts objects → JSON         |
| Error handling | Clean, readable error responses |

Core Concepts
  - Models: Define data structures using Python classes
  - Fields: Define attributes with types and constraints
  - Validators: Custom validation logic
  - Serialization: Convert models to/from JSON
Use Cases
  - API Data Validation
  - Configuration Management
  - Data Parsing and Serialization
  - Complex Data Structures


Request lifecycle:
- Client sends JSON
- FastAPI passes data to Pydantic
- Pydantic:
  - Validates
  - Converts
  - Raises errors if invalid
Your function gets clean Python object  

'''
from pydantic import BaseModel , EmailStr, AnyUrl , Field
from typing import List , Dict , Optional , Annotated
# create a user class with BaseModel

class User(BaseModel):
    name: str
    age: int=Field(..., gt=0 , description="Age must be greater than zero" , example=25 , strict=True) # you can add validation here , also strict=True will ensure that only int is allowed
    email: Annotated[EmailStr, Field(..., description="User   email address",title="Email Address",
    example=["user@example.com"] , default="user@example.com")] # pydantic has built in email type
    # create a user complex type with list and dict
    # BY default all fields are required in pydantic model
    # to make them optional we can use Optional from typing module

class ComplexUser(BaseModel):
    name: str
    age: int
    email: EmailStr # pydantic has built in email type
    skills: List[str]=Field(max_length=5) # you can also use list for skills
    address: Dict[str, str] # here also we are using dict for address
    optional_field:Optional[str] = None # this field is optional
    isMarried:Optional[bool] = False # default value is False
    #isMarried:bool=False # this field is required with default value False
    linkedIn:AnyUrl # pydantic has built in url type

# How to do data validation in pydantic
class ValidatedUser(BaseModel):
    name: str
    age: int
    email: EmailStr

    # you can add custom validation methods
    @classmethod
    def validate_age(cls, value):
        if value < 0:
            raise ValueError("Age must be a positive integer")
        return value

    @classmethod
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        return value




#how to use this User class in FastAPI


def create_user(user:User):
    return {
        "msg": "User created successfully",
        "user": user
    }

# Example usage
# what is unpack in python
# Unpacking in Python refers to the process of extracting values from data structures like lists, tuples, or dictionaries and assigning them to variables in a single statement. This is often done using the asterisk (*) for lists/tuples and double asterisk (**) for dictionaries.
# it is simlar to destructuring in JavaScript {...obj} = obj
new_user = User(name="Alice", age=30, email="alice@example.com")
result = create_user(new_user)
print(result)
# Output:
# {
#     "msg": "User created successfully",
#     "user": {
#         "name": "Alice",
#         "age": 30,
#         "email": "alice@example.com"
#     }
# }