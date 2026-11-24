# ❤️ Heart Disease Prediction API

A simple Machine Learning API built with **FastAPI**, containerized with **Docker**, and deployed on **Render**.

## Live Demo

**https://heart-diseases-api-3chy.onrender.com/docs**

## Endpoints

| Method | Endpoint   | Description                        |
| ------ | ---------- | ---------------------------------- |
| GET    | `/health`  | Health check                       |
| GET    | `/info`    | Model type & feature list          |
| POST   | `/predict` | Predict heart disease (true/false) |

## Example Request — `POST /predict`

```json
{
  "age": 63,
  "sex": 1,
  "cp": 3,
  "trestbps": 145,
  "chol": 233,
  "fbs": 1,
  "restecg": 0,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 2.3,
  "slope": 0,
  "ca": 0,
  "thal": 1
}
```
