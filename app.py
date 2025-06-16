from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("📨 Received data from frontend:", data)

        # Example logic
        hours = float(data.get('hours', 0))
        attendance = float(data.get('attendance', 0))
        sleep = float(data.get('sleep', 0))
        previous = float(data.get('previous', 0))

        if hours >= 10 and attendance >= 90 and sleep >= 7 and previous >= 85:
            result = "Pass with Distinction"
        elif hours >= 5 and attendance >= 75:
            result = "Pass"
        else:
            result = "Fail"

        print("✅ Prediction result:", result)
        return jsonify({'prediction': result})
    except Exception as e:
        print("❌ Error in backend:", str(e))
        return jsonify({'error': 'Prediction error.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
