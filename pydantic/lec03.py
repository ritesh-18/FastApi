# How to compute some value that you can get from other data fields 
# Example: if you have DOB then you can easily calculate his age 

from pydantic import BaseModel , EmailStr  , computed_field
from typing import List , Dist



class User(BaseModel):
    name : str
    dob:str

    @computed_field
    @property
    def age(self):
        yearval=self.dob.split("/")[-1]
        #now yearval has born year
        # calulate the diff of year from now and return
        age_val=10
        return age_val # now you can use age as a fields
    
'''
you can also use nested model 
meaning one model can use another model as a type

example 
one model is  Address , User

user{
   name :str
   address:Address # nested model
}


# how to export this model
  there are two ways: 
    - model_dump() 
    - json()

'''    
