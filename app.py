# app.py

from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# 📦 Load trained model and artifacts
cls_model = joblib.load('trained_data/model_cls.pkl')
features = joblib.load('trained_data/model_features.pkl')
result_encoder = joblib.load('trained_data/result_encoder.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # ✅ Convert input into DataFrame
    input_df = pd.DataFrame([data])

    # 🧠 Ensure all expected features are present
    input_df = input_df.reindex(columns=features, fill_value=0)

    # 🤖 Predict pass/fail
    cls_encoded = cls_model.predict(input_df)[0]
    result = result_encoder.inverse_transform([cls_encoded])[0]

    # 📨 Return result
    response = {
        "Prediction": result
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
