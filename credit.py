import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import pickle
from flask import  Flask,render_template,request
app = Flask(__name__, static_url_path='/static')
df = pd.read_csv('Loan_approvals.csv')
df.head(10)
df.info()
df.isnull().sum()
data = df.dropna()
data.isnull().sum()
data.replace({"Loan_Status": {'N': 0, 'Y': 1}}, inplace=True)
data.head()
data['Dependents'].value_counts()
data['Dependents'].replace({'3+', 4}, inplace=True)
data['Dependents'].value_counts()
"""# *Model*"""
label_encoder = preprocessing.LabelEncoder()
data['Gender'] = label_encoder.fit_transform(data['Gender'])
data['Married'] = label_encoder.fit_transform(data['Married'])
data['Education'] = label_encoder.fit_transform(data['Education'])
data['Self_Employed'] = label_encoder.fit_transform(data['Self_Employed'])
data['Property_Area'] = label_encoder.fit_transform(data['Property_Area'])
data['Loan_Status'] = label_encoder.fit_transform(data['Loan_Status'])
data.head()
X = data[['Gender', 'Education', 'ApplicantIncome', 'Credit_History', 'Property_Area']]
Y = data['Loan_Status']
print(X)
print(Y)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=2)
print(X.shape, X_train.shape, X_test.shape)
"""# *Model*"""
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, Y_train)
with open ('credit.pkl','wb') as file:
    pickle.dump(model,file)
Y_pred = model.predict(X_test)
print(classification_report(Y_test, Y_pred))
print(confusion_matrix(Y_test, Y_pred))
# print("Costumer Get : ", model.predict([[1, 0, 4583, 1.0, 0]]))
with open ('credit.pkl','rb') as file:
    model1 = pickle.load(file)
model1.predict([[1, 0, 4583, 1.0, 0]])
@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
     Gender = float(request.form['Gender'])
     Education = float(request.form['Education'])
     ApplicantIncome = float(request.form['ApplicantIncome'])
     Credit_History = float(request.form['Credit_History'])
     Property_Area = float(request.form['Property_Area'])
     result= model.predict([[Gender, Education, ApplicantIncome, Credit_History, Property_Area]])[0]
     return render_template('index.html',result="{}".format(result))
if __name__=="__main__":
    app.run(debug=True)


