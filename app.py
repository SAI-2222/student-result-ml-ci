
from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import pandas as pd
from pathlib import Path

app = FastAPI(title="Student Result Prediction API")

MODEL_PATH = Path("student_result_model.pkl")
model = joblib.load(MODEL_PATH)


class StudentInput(BaseModel):
    attendance: float = Field(ge=0, le=100)
    internal_marks: float = Field(ge=0, le=100)
    assignment_marks: float = Field(ge=0, le=100)
    previous_score: float = Field(ge=0, le=100)


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(student: StudentInput):
    features = pd.DataFrame([student.model_dump()])
    prediction = int(model.predict(features)[0])

    return {
        "prediction": prediction,
        "result": "PASS" if prediction == 1 else "FAIL"
    }
