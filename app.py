from fastapi import FastAPI, HTTPException
import pickle
import pandas as pd


app = FastAPI()

# Load the pickled pipeline
## YOUR CODE HERE
pipeline = 

"""
Define the prediction endpoint
1. Create a POST route named "predict" 
2. Define a funtion inside the route to 
    i receive the inference data
    ii. predict on the received data
    iii. return the predictions
"""

## YOUR CODE HERE
@app.post("/predict")
def predict(data: dict):
  data = data
  df = pd.DataFrame(data)

  return pipeline.predict(df)



# Inference Query
"""
curl -X 'POST' \
  'http://localhost:8000/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "alcohol": 12.3,
  "flavanoids": 2.8,
  "total_phenols": 2.5
}'
"""

