#使用scikit-learn的 SVC类，该类提供了定义模型并将模型与数据进行拟合的函数
from sklearn.sVm import  SVC
model= SVC()
model.fit(x_Values,y_ Values)
#在上述示例中，model变量是一个拟合到数据x_Values,y_ Values的支持向量机模型，拟合模型是指寻找拟合训练数据的最佳界限
#使用模型的predict()函数进行两项预测
print(model.predict([[0.2,0.8],[0.5,0.4]]))
#该模型返回了一个预测结果数组，每个输入数组一个预测结果。第一个输入[0.2,0.8]的预测结果为0
#第二个输入[0.5,0.4]的预测结果为1
#超参数
#定义模型时，可以指定超参数。最常见的超参数包括
#C：C参数
#kernel:内核。最常见的内核为linear,poly,和rbf
#degree:如果内核是多项式，则此参数为内核中的最大单项式次数
#gamma：如果内核是径向基函数，则此函数为γ参数
#例如，下面定义了一个次数为4C参数为0.1的多项式内核模型
model=SVC(kernel="poly",degree=4,C=0.1)
#支持向量机练习
#数据拆分为特征X和标签y
#需要完成以下步骤
#1构建支持向量机模型使用scikit-learn的SVC创建支持向量机分类模型并将其赋值给变量model
#2将模型与数据进行拟合
#如果有必要的话，指定一些超参数。目标是在数据集中获得100%的准确率，提示：并非所有内核都合适
#3使用模型进行预测
#预测训练集的标签，并将此列表赋值给变量y_pred
#4计算模型的准确率为此，使用sklearn函数accuracy_score
#注意：练习要求在训练集上准确率达到100%，当然，要小心过拟合！如果参数选择非常的值，你将很好的拟合训练集，
#但是可能并不是最好的模型。尝试寻找能够完成任务的最小可能参数，这样过拟合的几率就更小了
#Import statements
from sklearn.svm import SVC
from sklearn.metric import accuracy_score
import pandas as pd
import numpy as np

#Read the data
data=np.asarray(pd.read_csv("data.csv",header=None))
#Assign the features to the variable X,and the labels to the variable y.
X=data[:,0:2]
y=data[:,2]
#TODO:Create the model and assign it to the vairable model.
#Find the right parameters for this model to achie 100% accuracy on the dataset
model=SVC(kernel="rbf",gamma=27)

#TODO:Fit the model
model.fit(X,y)
#TODO:Make predictions.Store them in the variable y_pred
y_pred=model.predict(X)

#TODO:Calculate the accuracy and assign it to the variable acc
acc=accuracy_score(y,y_pred)
