# here we will load the pkl file and do predictions on given input
from fastapi import FastAPI, HTTPException
import json
from fastapi.responses import JSONResponse
import pickle
import pandas as pd
from typing import Literal 
#import pkl file and load it here (in production load pkl file only once when server starts not on every request)
# need to install scikit-learn and pandas if not already installed
# pickle → needs sklearn → sklearn not found → crash

with open("model.pkl" , "rb") as f:
    model=pickle.load(f)


# create an object of FastApi
app=FastAPI()


#here we are going to predict whether a particular person will buy insurance or not based on input features




#create a pydantic model for input data validation



@app.post("/predict")
def predict_insurance(data:dict):
    try:
        #convert input data to dataframe
        input_data=pd.DataFrame([data])
        
        #make prediction using the loaded model
        prediction=model.predict(input_data)
        
        #return the prediction result
        return JSONResponse(
            status_code=200,
            content={
                "prediction": int(prediction[0]),
                "status":200
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))