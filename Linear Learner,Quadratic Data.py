# In this exercise we'll examine a learner which has high bias,and is incapable of learning the patterns in the data
#learning the patterns in the data
#Use the learning curve function from sklearn.learning_curve to plot learning curves of both training and testing error
from sklearn.linear_model import LinearRegression
from sklearn.learning_curve import learning_curve
import matplotlib.pyplot as plt
from sklearn.metrics import explained_variance_score,make_scorer
from sklearn.cross_validation import KFold
import numpy as np

#set the learning curve parameters;you will need this for learning_vurves
size=1000
cv_sets=KFold(size,shuffle=True)
scorer=make_scorer(explained_variance_score)

#create a series of data that forces a learner to have high bias
#note for this quiz you do not need to create training and testing sets
X=np.reshape(np.random.normal(scale=2,size=size,(-1,1))
y=np.array([[1-2*x[0]+x[0]**2]for x in X])

def plot_curve():
    reg=LinearRegression()
    reg.fit(X,y)
    print "Regressor score:{:.4f}".format(reg.score(X,y))
    #TODO:Use learning_curve imported above to create learning curves form X and y.
    #You will need to ues 'cv_sets' and 'scorer' as parameters in the function
    
    train_sizes,train_scores,test_scores=(None,None,None)
    #ToDO;Plot the learning curves for boh the training scores and testing scores
    #Use plt.plot() twice--one for each score.Be sure to give them labels!
    #plt just 2(mean scores for training and testing)
    #You can use np.mean(train_scores,axis=1) to get mean train_scores values
    #similarly you can get the mean for the test_scores
    #plot aesthetics
    
    plt.ylim(-0.1,1.1)
    plt.ylabel("Curve Score")
    plt.xlabel("Training Points")
    plt.legend(bbox_to_anchor=（1.1，1.1））
    plt.show()
    
