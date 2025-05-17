from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Server is running!" 

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message', '').lower()

    if user_input == 'hi':  
        return jsonify({'response': 'Hello, Kyla!'})  
    else:
        return jsonify({'response': "I don't understand."})  
    
if __name__ == '__main__':
    app.run(debug=True)
