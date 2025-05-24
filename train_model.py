# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
import joblib
import os

# 📁 Ensure the trained_data directory exists
os.makedirs("trained_data", exist_ok=True)

# 📥 Load the student performance dataset
df = pd.read_csv('csv/StudentPerformanceFactors.csv')

# ✅ Define logic to classify Pass or Fail
def determine_result(row):
    if (row['Previous_Scores'] >= 75 and
        row['Hours_Studied'] >= 8 and
        row['Attendance'] >= 80 and
        row['Sleep_Hours'] >= 6 and row['Sleep_Hours'] <= 10): # <--- Sleep range
        return 'Pass'
    else:
        return 'Fail'

# 🏷️ Add the result column based on rule
df['Result'] = df.apply(determine_result, axis=1)

# 🎯 Set inputs (X) and output (y)
X_raw = df[['Hours_Studied', 'Attendance', 'Sleep_Hours', 'Previous_Scores']]
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df['Result'])

# 💾 Save label encoder for decoding predictions later
joblib.dump(label_encoder, 'trained_data/result_encoder.pkl')

# 🧠 Build the pipeline for training
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', MLPClassifier(
        hidden_layer_sizes=(64,),
        activation='relu',
        max_iter=2000,
        early_stopping=True,
        random_state=42
    ))
])

# 📊 Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_raw, y, test_size=0.2, random_state=42)

# 🚂 Train the model
pipeline.fit(X_train, y_train)

# 💾 Save model and feature list
joblib.dump(pipeline, 'trained_data/model_cls.pkl')
joblib.dump(X_raw.columns.tolist(), 'trained_data/model_features.pkl')

# ✅ Done
print("✅ Training complete. Model and encoders saved in 'trained_data/'")
