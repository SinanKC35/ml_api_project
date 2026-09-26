import xgboost as xgb
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "../models/xgboost_model.json")

model = xgb.XGBClassifier()
model.load_model(MODEL_PATH)

def predict_churn(data: dict):
    import pandas as pd
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]
    return int(prediction), float(probability)