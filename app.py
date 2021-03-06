import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from scipy.stats import zscore 

app = Flask(__name__)
model = pickle.load(open('model_dt.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
#     final_features_scaled = final_features.apply(zscore)
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('predict.html', prediction_text='${}'.format(output))
#     return redirect(url_for('index') + '#myModal', prediction_text=output)

if __name__ == "__main__":
    app.run(debug=True)
