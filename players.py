#importing the liabraries
import numpy as np
import pandas as pd
import pickle
from flask import  Flask,render_template,request
app = Flask(__name__, static_url_path='/static')
#reading the csv
df=pd.read_csv("E:\\movie imdb\\players.csv")
#importing sklearn liabraries
from sklearn.model_selection import train_test_split
#fitting the values in variables
x=df.iloc[:,6:10]
y=df.iloc[:,5]
#fitting the variables in models
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
#importing the model
from sklearn.svm import SVR
#fitting the model
model = SVR(kernel='poly',degree=5,C=2)
model.fit(x_train, y_train)
with open ('players.pkl','wb') as file:
    pickle.dump(model,file)
#predicting the value
y_pred = model.predict(x_test)
from sklearn.metrics import mean_absolute_error,mean_squared_error
MAE = mean_absolute_error(y_test,y_pred)
MAE
MSE = mean_squared_error(y_test,y_pred)
MSE
RMSE = np.sqrt(MSE)
RMSE
with open ('players.pkl','rb') as file:
    model1 = pickle.load(file)
model1.predict([[248, 48.52, 50817, 67.58]])
@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
     HS=float(request.form['HS'])
     AVE = float(request.form['AVE'])
     BF = float(request.form['BF'])
     SR = float(request.form['SR'])
     result= model.predict([[HS, AVE, BF, SR]])[0]
     return render_template('index.html',Runs="{}".format(result))
if __name__=="__main__":
    app.run(debug=True)

