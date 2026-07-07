"""
Model Prediction API
"""
import joblib
import pandas as pd
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import os

app = FastAPI(title="MLOps Prediction API")

# Load model
model_path = 'models/best_model.joblib'
if os.path.exists(model_path):
    model = joblib.load(model_path)
    print("✅ Model loaded successfully")
else:
    model = None
    print("⚠️ Model not found. Please run train.py first.")

class PredictionInput(BaseModel):
    features: Dict[str, float]
    
class BatchPredictionInput(BaseModel):
    features: List[Dict[str, float]]

@app.get("/")
async def root():
    return {
        "message": "MLOps Prediction API",
        "status": "running",
        "model_loaded": model is not None
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }

@app.post("/predict")
async def predict(input_data: PredictionInput):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        # Convert to array
        features = np.array([[v for v in input_data.features.values()]])
        prediction = model.predict(features)[0]
        return {
            "prediction": float(prediction),
            "features": input_data.features
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/predict/batch")
async def predict_batch(input_data: BatchPredictionInput):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        features = np.array([[v for v in item.values()] for item in input_data.features])
        predictions = model.predict(features)
        return {
            "predictions": [float(p) for p in predictions],
            "count": len(predictions)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
