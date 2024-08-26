# flask_ml_app/app.py

from flask import Flask, render_template, request, jsonify
from model.dummy_model import DummyModel  # Ensure the path to the model is correct

app = Flask(__name__)

# Instantiate the dummy model
model = DummyModel()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form['input_data']
            
        # Ensure the input is cast to the correct type, in this case an integer
    prediction = model.predict([int(data)])  # or model.predict([data]) if you handle it differently in the model
                        
    return jsonify({'prediction': prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)