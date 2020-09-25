import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from scipy.stats import zscore 

app = Flask(__name__)
model = pickle.load(open('model_dt.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    final_features_scaled = final_features.apply(final_features)
    prediction = model.predict(final_features_scaled)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Sale should be $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
