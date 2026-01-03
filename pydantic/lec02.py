# here lets talk about custom validator , transforms , and complex types in pydantic
from pydantic import BaseModel , EmailStr, AnyUrl , Field , field_validator , model_validator
from typing import List , Dict , Optional , Annotated

# create a user class with BaseModel
class User(BaseModel):
    name: str
    age: int=Field(..., gt=0 , description="Age must be greater than zero" , example=25 , strict=True) # you can add validation here , also strict=True will ensure that only int is allowed
    email: Annotated[EmailStr, Field(..., description="User email address",title="Email Address",
    example=["user@example.com"] , default="user@example.com")] # pydantic has built in email type

    @field_validator('age' , mode='after') # mode='after' means this validator will be called after the default validation (after type conversion) so if you pass age as string it will be converted to int first and then this validator will be called , default val=after
    @classmethod
    def validate_age(cls, value):
        # cls represents the class itself 
        if value > 18:
            raise ValueError("Age must be a greater than 18")
        return value

    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        return value
    # model_validator is used for multiple field dependent on each other
    @model_validator(mode="after")
    def validate_age_email(cls , model):
        if model.age<18 and model.email!="":
            raise ValueError("Email should be exist only for age >18")
