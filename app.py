import flask; print(flask.__version__)
from flask import Flask, render_template, request
import os
import numpy as np
import pickle
import statistics as stats

app = Flask(__name__)
app.env = "development"
result = ""
print("I am in flask app")

@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    print("Request.method:", request.method)
    print("Request.TYPE", type(request))
    print("In the process of making a prediction.")
    if request.method == 'POST':
        print(request.form)
        print("_-----")
        day1 = request.form['lag1']
        day1 = np.array([float(x) for x in day1.split(",")])
        
        day2 = request.form['lag2']
        day2 = np.array([float(x) for x in day2.split(",")])
        
        day3 = request.form['lag3']
        day3 = np.array([float(x) for x in day3.split(",")])
        day4 = request.form['lag4']
        day4 = np.array([float(x) for x in day4.split(",")])
        day5 = request.form['lag5']
        day5 = np.array([float(x) for x in day5.split(",")])
        
        test_arr = np.array([day1, day2, day3, day4, day5])
        model = pickle.load(open('ml_knn_model.pkl', 'rb'))
        print("Model Object: ", model)
        prediction = model.predict(test_arr)
        result = f"Based on the last 5 day laps the model has predicted that the market will go: {stats.mode(prediction)}"
        return render_template('index.html', result=result)
    return render_template('index.html')
app.run(host='0.0.0.0', port=5001, debug=False)
