from fastapi import FastAPI, HTTPException
import pickle
import pandas as pd

app = FastAPI()

# Load the pickled pipeline
with open('pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

@app.get("/")
def landing():
    return {"Content": "Interview-Assignment-Test"} 

# Define the prediction endpoint
@app.post("/predict/")
def predict(data: dict):
    try:
        # Convert input data to DataFrame
        df = pd.DataFrame([data])
        
        # Make prediction using the pipeline
        prediction = pipeline.predict(df)
        
        # Return prediction
        return {"prediction": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


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