#在sklearn中的网格搜索很简单，我们将使用一个例子来说明，假设想要训练支持向量机，别切在一下参数之间做出决定：
#kernel:poly和rbf
#C:0.1,1或10
#1.导入GridSearchCv
from sklearn.model_selection import GridSearchCv
#2选择参数：
#现在来选择想要的选择的参数，并形成一个字典。在这本字典中，键keys将是参数的名称，值（values）将是每个参数可能值得列表
parameters={"kernel":["poly","rbf"],"C":[0.1,1,10]}
#创建一个评分机制（scorer）
#需要确认将使用什么指标来为每个候选模型评分。这里将使用F1分数
from sklearn.metrics import make_scorer
from sklearn.metrics import f1_score
scorer=make_scorer(f1_score)
#4使用参数parameter和评分机制scorer创建一个GridSearch对象。使用此对象与数据保持一致(fit the data)
#create the object
grid_obj=GridSearchCv(clf,parameters,scoreing=scorer)
#Fit the data
grid_fit=grid_obj.fit(X,y)
#5.获得最佳估算器（estimator）
best_clf=grid_fit.best_estimator_
