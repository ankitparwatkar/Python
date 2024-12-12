import numpy as np
import pandas as pd

df=pd.read_csv("E:\movie imdb\ADANIPORTS.csv")

x=df.iloc[:,3:8].values
y=df.iloc[:,8].values

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

from sklearn.svm import SVR

model = SVR(kernel='poly',degree=2,C=2)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

from sklearn.metrics import mean_absolute_error,mean_squared_error

MAE = mean_absolute_error(y_test,y_pred)
MSE = mean_squared_error(y_test,y_pred)
RMSE = np.sqrt(MSE)

MAE

MSE

RMSE

model.predict([[440,770,1050,770,959]])









import pickle

# Save model to file
with open("iris_model.pkl", "wb") as f:
    pickle.dump(model, f)
    
    
    
    