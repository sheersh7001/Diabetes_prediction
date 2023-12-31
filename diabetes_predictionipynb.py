# -*- coding: utf-8 -*-
"""Diabetes_Predictionipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dYErz2EpwpG2F6RUAR8LHv_nLvxQqevd
"""

import pandas as pd
import numpy as np

dataset = pd.read_csv('/content/diabetes (1).csv')

dataset.head()

dataset.shape

dataset.describe()

dataset['Outcome'].value_counts()

dataset.groupby('Outcome').mean()

"""Now seprating the data and the labels

"""

x=dataset.drop(columns='Outcome', axis=1)
y = dataset['Outcome']

print(x)

print(y)

"""Now data Standardization"""

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(x)

standardize_data=scaler.transform(x)

"""Below We have another method for the same fit and transformation"""

# scaler.fit_transform(x)

print(standardize_data)

x=standardize_data
y=dataset['Outcome']

print(x)
print(y)

"""Now train test split"""

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2, stratify=y,random_state=2)

print(x.shape,x_train.shape,x_test.shape)

"""Now training the model"""

from sklearn import svm
classifier=svm.SVC(kernel='linear')

"""Now training the svm classifier"""

classifier.fit(x_train,y_train)

"""MODEL EVALUATION"""

from sklearn.metrics import accuracy_score
x_train_prediction=classifier.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction, y_train)

print('Accuracy score of the training data:', training_data_accuracy )

"""Now checking on the test data .It is more important to check on the test data as we already know the train data and by checking the accuracy on the test data we get that how well our model is working"""

x_test_prediction=classifier.predict(x_test)
test_data_accuracy=accuracy_score(x_test_prediction, y_test)

print('Accuracy score of the test data:', test_data_accuracy)

"""Making a predictive system"""

input_data=(7,100,0,0,0,30,0.484,32)
#changing the input data to numpy array
input_data_as_numpy_array=np.asarray(input_data)
#reshape the array as we are predicting for one array
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
#standardize the input data
std_data=scaler.transform(input_data_reshaped)
print(std_data)
prediction = classifier.predict(std_data)
print(prediction)
if(prediction[0]==0):
  print("The patient is not diabetic")
else:
  print("The patient is diabetic")

