from fastapi import FastAPI, Path , HTTPException , Query , Body , Request , Response
import json
from fastapi.responses import JSONResponse


# create an object of FastApi

app=FastAPI()


#helper function to load the json data
def load_json_data():
    with open("data.json" , "r") as f:
        data=json.load(f)
    print("Data loaded successfully" )    
    return data
    
def write_json_data(data):
    # write data to json file
    with open("data.json" , "w") as f:
        json.dump(data, f)
    return True

@app.get("/")
def read_root():
    return {
        "msg":"Welcome to FastAPI!",
        "status":200
    }
@app.get("/about")
def read_about():
    return {
        "msg":"About FastAPI",
        "status":200
    }
@app.get("/data")
def read_data():
    data=load_json_data()
    return {
        "data":data,
        "status":200
    }


# QueryParam: sort by age(required) and order(optional by default asc) in ascending or descending order
# from fastapi import Query, HTTPException

@app.get("/data/sort")
def read_data_sorted(
    sort_by: str = Query(
        ...,
        description="The field to sort by",
        example="age"
    ),
    order: str = Query(
        "asc",
        description="Sort order: asc or desc",
        example="desc"
    )
):
    data = load_json_data()

    # Validate order
    if order not in ("asc", "desc"):
        raise HTTPException(
            status_code=400,
            detail="order must be 'asc' or 'desc'"
        )

    try:
        sorted_data = sorted(
            data.values(),
            key=lambda x: x.get(sort_by),
            reverse=(order == "desc")
        )

        return {
            "data": sorted_data
        }

    except TypeError:
        raise HTTPException(
            status_code=400,
            detail=f"Field '{sort_by}' contains non-sortable values"
        )

    except KeyError:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort_by field: {sort_by}"
        )


# return the data based on patient_id
@app.get("/data/{patient_id}")
def read_data_by_patient_id(patient_id: str = Path(..., description="The ID of the patient to get data for" , example="P001")):
        data=load_json_data()
        if patient_id in data:
            return {
                "data":data[patient_id],
                "status":200
            }
        else: 
            raise HTTPException(status_code=404, detail="Patient ID not found")



# Now POST / PATCH / DELETE methods can be added here to create , update and delete the data
# How to use Body  , Request , Response in FastAPI
@app.post("/data")
def create_data(  new_data: dict = Body(... , description="New patient data to add" , example={
        "patient_id": "P008",
        "name":"Charlie-2",
        "age":29,
        "healthy":True,
        "location":"Germany",
        "occupation":"Mobile App Developer",
        "salary":70000,
        "skills":["Java","Kotlin","Swift","Flutter"]
})):
    data=load_json_data()
    patient_id=new_data.get("patient_id")
    if not patient_id:
        raise HTTPException(status_code=400, detail="patient_id is required in the request body")
    if patient_id in data:
        raise HTTPException(status_code=400, detail="Patient ID already exists")
    data[patient_id]=new_data
    write_json_data(data)
    # response.status_code=201
    # return {
    #     "msg":"Data created successfully",
    #     "data":new_data,
    #     "status":201
    # }
    return JSONResponse(status_code=201, content={
        "msg":"Data created successfully",
        "data":new_data,
    })

# create a pydantic model for update data , insert data in db , in fastapi no need to get data from request body , you can directly use the pydantic model to get the data from request body
'''
`Examples`:
            from pydantic import BaseModel

            class UserCreate(BaseModel):
                name: str
                age: int
                is_active: bool = True

            @app.post("/users")
            def create_user(user: UserCreate):
                return user
            Here, the `UserCreate` model defines the expected structure of the request body for creating a new user. FastAPI automatically parses the incoming JSON request body and populates an instance of `UserCreate`, which is then passed to the `create_user` function.


'''