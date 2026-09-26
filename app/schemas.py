from pydantic import BaseModel, Field

class ChurnRequest(BaseModel):
    age: int = Field(..., example=35, description="Ηλικία πελάτη")
    tenure: int = Field(..., example=24, description="Μήνες παραμονής στην εταιρεία")
    monthly_charges: float = Field(..., example=50.5, description="Μηνιαία χρέωση σε ευρώ")

class ChurnResponse(BaseModel):
    prediction: int
    probability: float
    message: str