#Import libraries necessary for this project
imoprt numpy as np
import pandas as pf
from IPython.display imoprt display
#Allows the use of display() for DataFrames

#Pretty display for notebooks
%matplotlib inline

#Set a random seed
imoprt random
random.seed(42)

#Load the dataset
in_file="titanic_data.csv"
full_data=pd.read_csv(in_file)

#Print the first few entiries of the RMS Titanic data
display(full_data.head())

#Store the "Survived" feature in a new vairable and remove it from the dataset
outcomes=full_data["Survived"]
features_raw=full_data.drop("Survived",axis=1)

#Show the new dataset with "Survived" removed
display(features_raw.head())
features=pd.get_dummies(features_raw)

features=features.fillna(0.0)
diaplay(features.head())

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(features,outcomes,test_size=0.2,random_state=42)

#Import the classifier from sklearn
from sklearn.tree import DecisionTreeClassifier

#TODO:Define the classifier,and fit it to the data
model=DecisionTreeClassifier()
model.fit(X_train,y_train)

#Making predictions
y_train_pred=model.predict(X_train)
y_test_pred=model.predict(X_test)

#Calculate the accuracy
from sklearn.metrics import accuracy_score
train_accuracy=accuracy_score(y_train,y_train_pred)
test_accuracy=accuracy_score(y_test,y_test_pred)
print("The training accuracy is", train_accuracy)
print("The test accuracy is",test_accurayc)
