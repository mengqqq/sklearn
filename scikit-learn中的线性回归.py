#线性回归
#在此部分，你将使用线性回归根据体质指数（BMI）预测预期寿命。在预测前，先了解一下构建此模型所需的工具
#对于线性回归模型，将使用scikit-learn中的LinearRegression类，此类会提供函数fit()来讲模型与数据进行拟合
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_values,y_values)
#在上述示例中，model变量拟合到数据x_values和y_values的线性回归模型。拟合模型意味着寻找拟合训练数据的最佳线条。使用模型的predict()函数做出两个预测。
print(model.predict([[127],[248]]))
#该模型返回了一个预测数组，每个输入数组一个预测结果，第一个输入[127]的预测结果是438.94308857.
#第二个输入[248]的预测结果是127.14839521.用[127]这样的数组（而不只是127）进行预测的原因是模型可以使用多个特征进行预测。
#线性回归练习
#在一下练习的bmi_and_life_expectancy.csv标签页中找到数据文件。它包含一下三列数据：
#country-样本的出生国家、地区
#life-expectancy-样本在该国家、地区的平均出生预期寿命
BMI-该国家、地区的男性BMI均值
#1加载数据
#数据位于文件bmi_and_life_expectancy.csv
#使用pandas read_csv将数据加载到数据帧中（别忘了导入pandas ）
#将数据帧赋值给变量bmi_life_data
@2构建线性回归模型
#使用scikit-learn中LinearRegression创建回归模型并将其赋值给bmi_life_model
#将模型与数据进行拟合
#使用模型进行预测
#使用值为21.07931的BMI进行预测，并将结赋值给变量laos_life_exp
#TODO:Add import statements
import pandas as pd
from sklearn.linear_model import LinearRegression
#Assign the dataframe to this variable
#TODO:Load the data
bmi_life_data=pd.read_csv("bmi_and_life_expectancy.csv")
#make the fit the linear regression model
#TODO:fit the model and assign it to bimi_life_model
bmi_life_model=LinearRegression()
bmi_life_model.fit(fmi_life_data[["BMI"]],bmi_life_data[["Life expectancy"]])
#make a prediction using the model
#TODO:Predict life expectancy for a BMI value of 21.07931
laos_life_exp=bmi_life_model.predict(21.07931)
