from flask import Flask, request, jsonify
import pickle
import numpy as np


import joblib

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the ML Prediction API!'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the request
        data = request.get_json()  # Expecting JSON with feature data
        
        # Ensure there are 5 features in the input
        if len(data['features']) != 5:
            return jsonify({'error': 'Expected 5 features, but got {}'.format(len(data['features']))})

        # Reshape the features into a 2D array (1 sample with 5 features)
        features = np.array(data['features']).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features)
        
        # Return prediction result
        return jsonify({'prediction': int(prediction[0])})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)


# {
#   "features": [440,770,1050,770,959]
# }

# features = np.array(data['features']).reshape(1, -1)

# if len(data['features']) != 5:
#     return jsonify({'error': 'Expected 5 features, but got {}'.format(len(data['features']))})
