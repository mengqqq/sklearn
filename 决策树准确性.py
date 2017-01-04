import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import numpy as np
import pylab as pl
features_train,labels_train,features_test,labels_test=makeTerrainData()

####your code goes here
acc=### you fill this in !
###be sure to compute the accuracy on the test set
def submitAccuracies():
    return{"acc":round(acc,3)}
    





from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier(random_state=0)
iris=load_iris()
cross_val_score(clf,iris.data,iris.target,cv=10)


apply(X[,check_input])                              he leaf that each sample is predicted as
decision_path(X[,check_input])
