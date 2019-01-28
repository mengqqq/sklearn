from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier()
model.fit(x_values,y_values)
#上述示例中，model变量是一个拟合到数据x_values 和y_values的决策树模型。拟合模式是秩寻找拟合训练数据的最佳线条。
#使用模型predict()函数进行两项预测
print(model.predict([[0.2,0.0],[0.5,0.4]]))
#超参数
#定义模型时，可以指定超参数，在实践中，最常见的参数包括：
#max_depth:数中的最大层级数量
#min_samples_leaf:叶子允许的最低样本数量
#min_samples_split:拆分内部节点所需的最低样本数量
#max_features:寻找最佳拆分方法时要考虑的特征数量

#在此示例中，定义了一个模型：树的最大深度max_depth为7，每个叶子的最低元素数量min_samples_leaf是10
model=DecisionTreeClassifier(max_depth=7,min_samples_leaf=10)
#需要完成的事项：
#1构建决策树模型，使用scikit-learn的DecisionTree构建决策树分类模型，并将其赋值给变量model
#2将模型与数据进行拟合
#   不需要指定任何超参数，因为默认的超参数将以100%的准确率拟合数据，但是，建议时间这些超参数
#   例如max_depth和min_samples_leaf,并尝试找到最简单的潜在模型，即最不太可能过拟合的模型
#3使用模型进行预测
#   预测训练集的标签，并将此列表赋值给变量y_pred
#4计算模型的准确率
#   为此，使用sklearn函数accuracy_score

#Import statements
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
#read the data
data=np.asarray(pd.rad_csv("data.csv",header=None))
#Assign the features to the variable X,and the labels to the variable y.
X=data[:,0:2]
y=data[:,2]
#TODO:Create the decision tree model and assign it to the variable model.
model=DecisionTreeClassifier()
$TODO:Fit the model
model.fit(X,y)
#TODO:Make predictions.Store them in the variable y_pred
y_pred=model.predict(X)
#TODO:Calulate the accuracy and assign it to the variable acc.
acc=accuracy_score(y,y_pred)
