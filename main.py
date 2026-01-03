from fastapi import FastAPI, Path , HTTPException , Query
import json


# create an object of FastApi

app=FastAPI()


#helper function to load the json data
def load_json_data():
    with open("data.json" , "r") as f:
        data=json.load(f)
    print("Data loaded successfully" )    
    return data
    
def append_json_data(data):
    # append data to json file at the end
    with open("data.json" , "a") as f:
        json.dump(data, f)
    f.write("\n")
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
from fastapi import Query, HTTPException

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

