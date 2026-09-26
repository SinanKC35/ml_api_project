# 🚀 Customer Churn Prediction - MLOps REST API

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.103.1-009688.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-2.0.0-orange.svg)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED.svg)
![Postman](https://img.shields.io/badge/Postman-Tested-FF6C37.svg)

## 🎯 Ο Σκοπός του Project
Σκοπός αυτού του project είναι η ανάδειξη της μετάβασης από την απλή Επιστήμη Δεδομένων (ένα στατικό Jupyter Notebook) στην **Παραγωγή (MLOps)**. 

Ένα μοντέλο Μηχανικής Μάθησης δεν έχει αξία αν δεν μπορεί να επικοινωνήσει με τον έξω κόσμο. Εδώ, αναπτύξαμε ένα σύστημα πρόβλεψης αποχώρησης πελατών (Customer Churn) και το μετατρέψαμε σε ένα πλήρως λειτουργικό, ανεξάρτητο Microservice. Οποιοδήποτε σύστημα (CRM, Web, Mobile App) μπορεί πλέον να του στείλει τα δεδομένα ενός πελάτη και να λάβει σε πραγματικό χρόνο την εκτίμηση κινδύνου.


## 🏗️ Τι Υλοποιήσαμε (Βήμα - Βήμα)

1. **Εκπαίδευση & Ασφαλής Εξαγωγή του Μοντέλου:** 
   Εκπαιδεύσαμε έναν αλγόριθμο XGBoost. Αποφύγαμε το παραδοσιακό `pickle` format, το οποίο είναι ασταθές και προκαλεί C-level memory crashes, και αποθηκεύσαμε το μοντέλο στο εγγενές `.json` format του XGBoost για απόλυτη σταθερότητα.
2. **Ανάπτυξη REST API:** 
   Χρησιμοποιήσαμε το **FastAPI** για τη δημιουργία των endpoints. Ενσωματώσαμε το **Pydantic** για αυστηρό Data Validation, ώστε το σύστημα να απορρίπτει λάθος τύπους δεδομένων πριν φτάσουν στον αλγόριθμο.
3. **Containerization:** 
   Κλείσαμε όλη την εφαρμογή σε ένα **Docker Container**. Ρυθμίσαμε τις εξαρτήσεις συστήματος (π.χ. `libgomp1` στο Linux) και κλειδώσαμε τις εκδόσεις των βιβλιοθηκών, λύνοντας το πρόβλημα *"σε εμένα δουλεύει, σε σένα όχι"*.
4. **Τελικές Δοκιμές (Testing):** 
   Ελέγξαμε διεξοδικά το σύστημα μέσω του **Postman**, προσομοιώνοντας πραγματικά POST requests και διασφαλίζοντας ότι ο server διαχειρίζεται σωστά την κίνηση, επιστρέφοντας άμεσα το τελικό JSON αποτέλεσμα με Status 200 OK.

---

## 📂 Δομή του Συστήματος
ml_api_project/
├── app/
│   ├── main.py          # Η κεντρική εφαρμογή και το Routing
│   ├── ml_service.py    # Φόρτωση του JSON μοντέλου & λογική πρόβλεψης
│   └── schemas.py       # Pydantic validation schemas
├── models/              # Φάκελος εκπαιδευμένων μοντέλων (Git Ignored)
├── train.py             # Script εκπαίδευσης XGBoost
├── Dockerfile           # Οδηγίες πακεταρίσματος
└── requirements.txt     # Βιβλιοθήκες και dependencies

⚙️ Οδηγίες Εκτέλεσης (Πώς να το τρέξετε)
Βήμα 1: Τοπική παραγωγή του εκπαιδευμένου μοντέλου

python3 train.py

Βήμα 2: Χτίσιμο και Εκκίνηση του Docker Container

Πρωτα

sudo docker build -t churn-ml-api .

Μετα 

sudo docker run -p 8000:8000 churn-ml-api

Όταν τελειωσει , παμε στο Google και γραφουμε http://localhost:8000/predict

Όταν το Docker ξεκινήσει, το API ακούει στη διαδρομή POST http://localhost:8000/predict. Μπορείτε να το τεστάρετε μέσω Postman ή Swagger UI (στο /docs).

Τα δεδομένα εισόδου (Request Body - JSON):
{
  "age": 35,
  "tenure": 24,
  "monthly_charges": 50.5
}
Το αποτέλεσμα που επιστρέφει το API (Response 200 OK):
{
    "prediction": 0,
    "probability": 0.005846,
    "message": "Χαμηλός κίνδυνος"
}
