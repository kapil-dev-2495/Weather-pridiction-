from flask import Flask,render_template,request
import requests
import pickle
import numpy as np
import pandas


app=Flask(__name__)
loadedModel=pickle.load(open('weatherHistory.sav','rb'))

@app.route("/" ,methods=['GET'])
def Home():
    return  render_template('WeatherPrediction.html')
    
    
@app.route("/predict" ,methods=['POST'])
def predict():
    Humidity=float(request.form['Humidity'])
    Visibility=float(request.form['Visibility'])
    Pressure=float(request.form['Pressure'])


    print("Humidity:",Humidity)
    print("Visibility:",Visibility)
    print("Pressure:",Pressure)

    
    prediction=loadedModel.predict([[ Humidity, Visibility, Pressure]])[0]
    #output=round(prediction,2)
    print(prediction)
    prediction = round(prediction, 2)
    #print(output)
    
    return render_template('WeatherPrediction.html',Temperature=prediction)
if __name__=='__main__' :
    app.run(debug=True)
    
