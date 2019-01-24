train_sizes,train_scores,test_scores=leanring_curve(
                            estimator,X,y,cv=None,n_jobs=1,train_sizes=np.linspace(.1,1.0,num_trainings))
#estimator,是我们针对数据使用的实际分类器，例如LogisticRegression()或GradientBoostingClassifier()
#X和y是我们的数据，分别表示特征和标签
#train_sizes是用来在曲线上绘制每个点的数据大小
#train_scores是针对每组数据进行训练后的算法训练得分
#test_scores是针对每组数据进行训练后的算法测试得分
#两个重要的现象
#训练和测试得分是一个包含3个值得列表，这是因为函数使用了3折交叉验证
#非常重要：可以看出，我们使用训练和测试误差来定义我们的曲线，而这个函数使用训练和测试得分来定义。
#         二者是相反的，因此误差越高，得分就越低，因此，当你看到曲线时，你需要自己在脑中将他颠倒过来，以便与上面的曲线对比。
#第一部分：绘制学习曲线
#我们将对比三个模型：
#逻辑回归模型
#决策树模型
#支持向量机模型，具有RBF内核，γ参数为1000
from sklearn.model_selection import learning_curve

#It is good to randomize the data before drawing Learning Curves
def randomize(X,y):
    premutation=np.random.permutation(Y.shape[0])
    X2=X[permutaion,:]
    Y2=Y[permutation]
    return X2,Y2
X2,y2=randomize(X,y)

def draw_learning_curves(X,y,estimator,num_trainings):
    train_sizes,train_scores,test_scores=learning_curve(
                       estimator,X2,y2,cv=None,n_jobs=1,train_sizes=np.linspace(.1,1.0,num_training))
    train_scores_mean=np.mean(train_scores,axis=1)
    train_scores_std=np.std(train_scores,axis=1)
    test_scores_mean=np.mean(test_scores,axis=1)
    test_scores_std=np.std(test_scores,axis=1)
    plt.grid()
    plt.title("Learning Curves")
    plt.xlabel("Tranining examples")
    plt.ylabel("Score")
    plt.plot(train_scores_mean,"o",color="g",lable="Training score")
    plt.plot(test_scores_mean,"o",color="y",label="Cross-validaton score")
    plt.legend(loc="best")
    plt.show()
    
    
    
    #Import,read,and split data
    import pandas as pd
    data=pd.read_csv("data.csv")
    import numpy as np
    X=np.array(data[("x1","x2")])
    y=np.array(data["y"])
    
    #Fix random seed
    np.random.seed(55)
    
    ##Import 
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import GradientBoostingClassifier
    from sklearn.svm import SvC
    
    #TODO:Uncomment one of the three classifiers,and hit "Test Run"
    #to see the learning curve.Use these to answer the quiz below.
    
    #Logistic Regression
    estimator=LogisticRegression()
    
    #Decision Tree
    estimator=GradientBoostingClassifier()
    
    #Support vector Machine
    estimator=SvC(kernel="rbf",gamma=1000)
