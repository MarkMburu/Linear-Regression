import numpy as np
import pandas as pd
import sklearn 
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as plt

data = pd.read_csv("student-mat.csv",sep=";")

data = data[["G1","G2","G3","studytime","failures","absences"]] #Dataframe

predict = "G3" #label

x = np.array(data.drop([predict],1)) #features or attributes

y = np.array(data[predict])

x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(x,y,test_size=0.1)

linear = linear_model.LinearRegression()

linear.fit(x_train,y_train)

acc = linear.score(x_test,y_test) #accuracy 

print(acc)

print("coefficient",linear.coef_)

print("intercept",linear.intercept_)

predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(predictions[x],x_test[x],y_test[x])


