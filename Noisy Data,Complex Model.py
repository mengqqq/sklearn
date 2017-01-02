# In this exercise we'll examine a learner which has high variance,and tries to learn nonexistant patterns in the data
Use the learning curve function from sklearn.learning_curve to plot learing curves of both training and testing error
from sklearn.tree import DecisionTreeRegressor 
import matplotlib.pyplot.pyplot as plt
from sklearn.learning_curve import learning_curve
from sklearn.cross_validation import KFold
from sklearn.metrics import explained_variance_score,make_scorer
import numpy as np
#set the learning curve parameters;you will need this for learning_curves
sie=1000
cv=KFold(size,shuffle=True)
score=make_scorer(explained_variance_score)
#create a series of data that forces a learner to have high variace
X=np.round(np.reshape(np.random.normal(scale=5,size=2*size),(-1,2)),2)
y=np.array([[nnp.sin(x[0]+np.sin(x[1]))] for x in X])
def plot_curve():
    reg=DecisionTreeRegressor()
    reg.fit()
    print "Regressor score:{:.4f}".format(reg.score(X,y))
#TODO Use learning_curve imported above to create learning curves for both the training data and testing data.you will need 'size','cv' 
#and 'score' from above.
training_sizes,training_scores,testing_scores=(None,None,None)
#TODO:Plot the training curves and the testing curves Use plt.plot twice--one for each score.Be sure to give them labels!
#plt aesthethic
plt.ylim(-0.1,1.1)
plt.ylabel("Curve Score")
plt.xlabel("Training Points")
plt.legend(bbox_to_anchor=(1.1,1.1))
plt.show()
