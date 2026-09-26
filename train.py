import pandas as pd
import xgboost as xgb
import os
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

print("Δημιουργία δεδομένων...")
X, y = make_classification(n_samples=1000, n_features=3, n_informative=3, n_redundant=0, random_state=42, class_sep=0.8, weights=[0.7, 0.3])
df = pd.DataFrame(X, columns=['age', 'tenure', 'monthly_charges'])
df['age'] = (df['age'] * 10 + 40).astype(int).clip(18, 80)
df['tenure'] = (df['tenure'] * 15 + 30).astype(int).clip(0, 72)
df['monthly_charges'] = (df['monthly_charges'] * 20 + 60).clip(10, 150)
df['churn'] = y

X_train, X_test, y_train, y_test = train_test_split(df[['age', 'tenure', 'monthly_charges']], df['churn'], test_size=0.2, random_state=42)

print("Εκπαίδευση μοντέλου...")
model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

os.makedirs('models', exist_ok=True)
model.save_model('models/xgboost_model.json')
print("ΕΠΙΤΥΧΙΑ! Το μοντέλο δημιουργήθηκε στο models/xgboost_model.json")
