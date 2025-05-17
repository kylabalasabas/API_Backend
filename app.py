from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Flask backend is running."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message', '').lower()

    if user_input == 'hi':
        return jsonify({'response': 'hello'})
    else:
        return jsonify({'response': f'You said: {user_input}'})

if __name__ == '__main__':
    app.run(debug=True)
