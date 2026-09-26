# 🚀 Customer Churn Prediction - MLOps REST API

## 🎯 Project Goal

The purpose of this project is to highlight the transition from basic Data Science (a static Jupyter Notebook) to **Production (MLOps)**.

A Machine Learning model has no value if it cannot communicate with the outside world. Here, we developed a Customer Churn prediction system and transformed it into a fully functional, independent Microservice. Any system (CRM, Web, Mobile App) can now send it a customer's data and receive a real-time risk assessment.

## 🏗️ What We Implemented (Step-by-Step)

1. **Model Training & Safe Export:**
We trained an XGBoost algorithm. We avoided the traditional `pickle` format, which is unstable and causes C-level memory crashes, and saved the model in XGBoost's native `.json` format for absolute stability.
2. **REST API Development:**
We used **FastAPI** to create the endpoints. We integrated **Pydantic** for strict Data Validation, ensuring the system rejects incorrect data types before they reach the algorithm.
3. **Containerization:**
We packaged the entire application in a **Docker Container**. We configured the system dependencies (e.g., `libgomp1` on Linux) and pinned the library versions, solving the *"it works on my machine"* problem.
4. **Final Testing:**
We thoroughly tested the system via **Postman**, simulating real POST requests and ensuring the server handles traffic correctly, instantly returning the final JSON result with a Status 200 OK.

---

## 📂 System Structure

```text
ml_api_project/
├── app/
│   ├── main.py          # The main application and Routing
│   ├── ml_service.py    # Loading the JSON model & prediction logic
│   └── schemas.py       # Pydantic validation schemas
├── models/              # Trained models folder (Git Ignored)
├── train.py             # XGBoost training script
├── Dockerfile           # Packaging instructions
└── requirements.txt     # Libraries and dependencies

```

## ⚙️ Execution Instructions (How to run it)

**Step 1: Local generation of the trained model**

```bash
python3 train.py

```

**Step 2: Build and Start the Docker Container**

First:

```bash
sudo docker build -t churn-ml-api .

```

Then:

```bash
sudo docker run -p 8000:8000 churn-ml-api

```

Once finished, go to your browser and type: `http://localhost:8000/predict`

When Docker starts, the API listens on the `POST http://localhost:8000/predict` route. You can test it via Postman or Swagger UI (at `/docs`).

**Input data (Request Body - JSON):**

```json
{
  "age": 35,
  "tenure": 24,
  "monthly_charges": 50.5
}

```

**The result returned by the API (Response 200 OK):**

```json
{
    "prediction": 0,
    "probability": 0.005846,
    "message": "Low risk"
}

```
