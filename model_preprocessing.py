'''
Lets's train a simple model related to its '''

import joblib #pikel also work as joblib it is used to convert result in binary
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris


#load dataset

data = load_iris()
X,y = data.data, data.target


#train the model

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, 'soumita.joblib')

