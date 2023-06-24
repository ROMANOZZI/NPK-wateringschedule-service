
import xgboost as xgb
# Feature scaling
from joblib import  load
from fastapi import FastAPI
from mangum import Mangum
import uvicorn
import json


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
   return int(prediction)

if __name__ == '__main__':
   import uvicorn
    
   uvicorn.run("main:app",  port=9000, log_level="info")
handler = Mangum(app)




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
