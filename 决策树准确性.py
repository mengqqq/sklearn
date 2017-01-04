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


apply(X[,check_input])                        Returns the index of the leaf that each samplpe is predicted as.
decision_path(X[,check_input])                Return the decision path in the tree
fit(X,y[,sample_weight,check_input,...])      Build a decision tree classifier from the training set(X,y).
fit_trainsform(X[,y])                         Fit to data,then transform it.
get_params([deep])                            Get parameters for this estimator.
predict(X[,check_input])                      Predict class or regression value for X
predict_log_proba(X)                          Predict class log-probabilities of the input samples X.
predict_proba(X[,check_input])                Predict class probabilities of the input samples X.
score(X,y[,sampe_weight])                     Returns the mean accuracy on the given test data and labels.
set_params(\*\*params)                        Set the parameters of this estimator
transform(\*args,\*\*kwargs)                  DEPRECATED:Support to use estimators as features selectors will be removed in version 0.19
