import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from flask import  Flask,render_template,request
app = Flask(__name__, static_url_path='/static')
df= pd.read_csv("D:\heart_disease\dataset.csv")
x=df.iloc[:,0:-1]
y=df.iloc[:,-1]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x_train,y_train)
with open ('disease.pkl','wb') as file:
    pickle.dump(model,file)
y_pred=model.predict(x_test)
from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))
with open ('disease.pkl','rb') as file:
    model = pickle.load(file)
model.predict([[63,1,3,145,233,1,0,150,0,2,0,0,1]])
@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/predict', methods=["POST"])
def predict():
     age = float(request.form['age'])
     sex = float(request.form['sex'])
     cp = float(request.form['cp'])
     trestbps = float(request.form['trestbps'])
     chol = float(request.form['chol'])
     fbs = float(request.form['fbs'])
     restecg = float(request.form['restecg'])
     thalach= float(request.form['thalach'])
     exang = float(request.form['exang'])
     oldpeak = float(request.form['oldpeak'])
     slope = float(request.form['slope'])
     ca = float(request.form['ca'])
     thal = float(request.form['thal'])
     result = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])[0]
     return render_template('index.html',result="{}".format(result))
if __name__=="__main__":
    app.run(debug=True)
