from fastapi import FastAPI, Query, HTTPException
import joblib 
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

class SepsisFeatures(BaseModel):
    PRG: float
    PL: float
    PR: float
    SK: float
    TS: float
    M11: float
    BD2: float
    Age: float
    Insurance: object
    

# Load models and encoder
## NB: putting models in models folder isnt working so i put them in the api folder

try:
    XGBoost = joblib.load("XGBoost.pkl")
    Logistic_Regressor = joblib.load("Logistic_Regression.pkl")
    encoder = joblib.load("label_encoder.pkl")
except Exception as e:
    print(f"Error loading models or encoder: {e}")
    raise


@app.get("/")
def status_check(): 
    return {"Status": "Api is online"}


@app.get("/documents")
def documentation():
    return {"All Documentation": "API Doumentation"}


@app.post("/XGBoost_prediction")
def predict_sepsis(data: SepsisFeatures):
     df = pd.DataFrame([data.model_dump()])

     prediction = XGBoost.predict(df)
     probability = XGBoost.predict_proba(df)

     prediction = int(prediction[0])

     prediction = encoder.inverse_transform([prediction])[0]

     if prediction == "Negative":
         probability = f'{round(probability[0][0], 2)*100}%'
     else:
         probability = f'{round(probability[1][0], 2)*100}%'

     return {"Prediction": prediction, "Probability": probability}


@app.post("/Logistic_Regressor")
def predict_sepsis(data: SepsisFeatures):
     df = pd.DataFrame([data.model_dump()])

     prediction = Logistic_Regressor.predict(df)
     probability = Logistic_Regressor.predict_proba(df)

     prediction = int(prediction[0])

     prediction = encoder.inverse_transform([prediction])[0]

     if prediction == "Negative":
         probability = f'{round(probability[0][0], 2)*100}%'
     else:
         probability = f'{round(probability[1][0], 2)*100}%'

     return {"Prediction": prediction, "Probability": probability}


##uvicorn api:app --reload