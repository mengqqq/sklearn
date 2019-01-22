#支持向量机
#在sklearn中只需要定义分类器，只需要定义分类器，然后使用下面这行代码使分类器与数据拟合（称为X,y）
classifier.fit(X,y)
#以下是我们定义的主分类器，以及必须导入的文件包
#逻辑回归
from sklearn.linear_model import LogisticRegression
classifier=LogisiticRegression()
#神经网络
from sklearn.neural_network import MLPClassifier
classifier=MLClassifier()
#决策树
from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier()
#支持向量机
from sklearn.svm import SVC
classifier=SVC()
#示例：逻辑回归
#从头到尾看看如何读取数据和训练分类器，假设使用上一部分的X和y，然后一下命令将训练逻辑回归分类器：
from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(X,y)
#训练一个你自己的模型
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
#Logistic Regression Classifier
classifier=LogisticRegression()
classifier.fit(X,y)
#Decision Tree Classifier
classifier=DecisionTreeClassifier()
classifier.fit(X,y)
#Support Vector Machine Classifier
classifier=SVC()
classifier.fit(X,y)

