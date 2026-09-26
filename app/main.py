from fastapi import FastAPI
from app.schemas import ChurnRequest, ChurnResponse
from app.ml_service import predict_churn

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Ένα ML API που προβλέπει αν ένας πελάτης θα αποχωρήσει χρησιμοποιώντας XGBoost.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Το API λειτουργεί! Πηγαίνετε στο /docs για το Swagger UI."}

@app.post("/predict", response_model=ChurnResponse)
def predict(request: ChurnRequest):
    data_dict = request.model_dump()
    
    pred, prob = predict_churn(data_dict)
    
    msg = "Υψηλός κίνδυνος αποχώρησης" if pred == 1 else "Χαμηλός κίνδυνος"
    
    return ChurnResponse(
        prediction=pred,
        probability=prob,
        message=msg
    )
