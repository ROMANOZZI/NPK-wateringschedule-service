
import xgboost as xgb
# Feature scaling
from joblib import  load
from fastapi import FastAPI
from mangum import Mangum

import json
import pickle


app=FastAPI()





@app.get('/predictNPK')
def predict(matrix: str):
   matrix=json.loads(matrix)
   
   sc = load('models/sscaler.joblib')
   bst=xgb.Booster()
   bst.load_model('models/NPK.model')
   new_data=sc.transform([matrix])
   new_data = xgb.DMatrix(new_data)
   prediction = bst.predict(new_data)
   return {"prediction":int(prediction)}
@app.get('/predictWatering')
def Predict(params:str):
   params=json.loads(params)
   with open('models/knn_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
   with open('models/scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)
   params=scaler.transform([params])
   prediction = loaded_model.predict(params)
   return {"prediction":int(prediction)}

   
   
@app.get('/predictWatering')
def Predict(params:str):
   params=json.loads(params)
   with open('models/knn_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
   with open('models/scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)
   params=scaler.transform([params])
   prediction = loaded_model.predict(params)
   return {"prediction":int(prediction)}

   
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app ,host="127.0.0.1",port=9000)




#  intialization:s1 :mixer 100% to the soil
# water + NPK 
# I s2: idle
# w S3 : 200ml 15ms water 
# N (N*) ml N 1800ms
# P 3 ml P 5400ms
# k 3 ml K 5400ms
# I s4: idle


# users
# site units
# status -
#          \- count:26 14
# temprature
# humidity
# soil moisture 

