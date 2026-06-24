from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import re

app = FastAPI()

model = joblib.load("spam_detector.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

class EmailRequest(BaseModel):
    email: str

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

@app.get("/")
def home():
    return {"message": "Spam Detection API Running"}

@app.post("/predict")
def predict(request: EmailRequest):

    text = clean_text(request.email)

    vector = vectorizer.transform([text])

    prediction = model.predict(vector)[0]

    return {
        "prediction": "Spam" if prediction == 1 else "Ham"
    }