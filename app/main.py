import joblib
import uvicorn
import numpy as np
import pandas as pd
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI(
    title='Car Price Prediction',
    version='1.0',
    description='Linear Regression model is used for prediction'
    )

model = joblib.load("LinearRegressionModel.joblib")

class Data(BaseModel):
    name: str
    year: int
    kms_driven: float
    fuel_type: str
    Company: str

# Api root or home endpoint
@app.get('/')
@app.get('/home')
def read_home():
    """
     Home endpoint which can be used to test the availability of the application.
     """
    return {'message': 'System is healthy'}

# ML API endpoint for making prediction aganist the request received from client
@app.post("/predict")
def predict(data: Data):

    result = model.predict(pd.DataFrame(columns=['name','year','kms_driven','fuel_type','Company'],data=np.array([data.name,data.year,data.kms_driven,data.fuel_type,data.Company]).reshape(1,5)))[0]
    return result

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
