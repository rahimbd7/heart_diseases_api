from fastapi import FastAPI
from app.schemas import HeartInput, PredictionOutput
import joblib
import numpy as np
import os

app = FastAPI(title="Heart Disease Prediction API")

MODEL_PATH = os.path.join(
    os.path.dirname(__file__), "..", "model", "heart_model.joblib"
)
model = joblib.load(MODEL_PATH)

FEATURE_NAMES = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal"
]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/info")
def info():
    return {
        "model_type": type(model).__name__,
        "features": FEATURE_NAMES,
        "target": "heart_disease (0=No, 1=Yes)"
    }

@app.post("/predict", response_model=PredictionOutput)
def predict(data: HeartInput):
    features = np.array([[
        data.age, data.sex, data.cp, data.trestbps, data.chol,
        data.fbs, data.restecg, data.thalach, data.exang,
        data.oldpeak, data.slope, data.ca, data.thal
    ]])
    prediction = model.predict(features)[0]
    return PredictionOutput(heart_disease=bool(prediction))