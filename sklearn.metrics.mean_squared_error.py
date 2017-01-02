from sklearn.metrics import mean_squared_error
y_true=[3,-0.5,2,7]
y_pred=[2.5,0.0,2,8]
mean_squared_error(y_ture,y_pred)//-.375
y_true=[[0.5,1],[-1,1],[7,-6]]
y_pred=[[0,2],[-1,2],[8,-5]]
mean_squared_error(y_true,y_pred)//0.708
mean_squared_error(y_true,y_pred,multioutput='raw_values')//array([0.416...,1.])
mean_squared_error(y_true,y_pred,multioutput=[0.3,0.7])//0.824
