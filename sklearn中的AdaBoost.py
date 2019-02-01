#在sklearn中建立AdaBoost模型与其他模型相同。可以使用scikit-learn的AdaBoost Classifier类,该类提供函数来定义你的模型，并将模型与数据进行拟合
from sklearn.esnemble import AdaBoostClassifier
model=AdaBoostClassifier()
model.fit(x_train,y_train)
model.predict(x_test)
#在上面的示例中，model变量是一个决策树模型，它与数据x_values和y_values进行拟合。函数fit和predict的功能与之前相同
#超参数
#定义模型的时候，可以确定超参数。在实际操作中，最常见的超参数为：
#base_estimator：若学习器使用的模型（切勿忘记导入该模型）
#n_estimators:使用的若学习期的最大数量
#比如在下面的例子中，定义了一个模型，它使用max_depth为2的据测算作为弱学习器，并且它雨荨的弱学习器的最大数量为4
from sklearn.tree import DecisionTreeClassifier
model=AdaBoostClassifier(base_estimator=DecisionTreeClassifier(max_depth=2),n_estimators=4)
