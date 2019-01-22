#试着用SVM分类器拟合此数据，如下所示：
classifier=SVC()
classifier.fit(X,y)
#如果输入上述内容，将失败（你将有机会在下面试试）。但是，也许我们没有充分利用SVM分类器。
#首先，我们使用了正确的内核吗？例如，我们可以使用2此多项式内容，如下所示：
classifier=SVC(kernel="poly",degree=2)
#我们自己试试，看看这些参数，稍后我们将深入了解这些参数，但是你可以设定以下这些值
#kernel:linear(线性)，poly（多项式），rbf（高斯核）
#degree:多项式内核的次数（如果选择了多项式内核）
#gamma:γ参数
#C：C参数
#在下面练习中，你可以试试这些参数，试着调整这些参数病使他们能够画出期望的界限区域
import pandas 
import numpy 
#Read the data
data=pandas.read_csv("data.csv")
#Split the data into X and y 
X=numpy.array(data[["x1","x2"]])
y=numpy.array(data["y"])
#Import the SVM Classifier
from sklearn.svm import SVC
#TODO:Define your classifier.
#Play with different values for these,from the options above.
#Hit "Test Run" to see how the classifier fit your data
#Once you can correctly classify all the points,hit "Submit"
classifier=SVC(kernel="rbf",gamma=200)
#Fit the classifier
classifier.fit(X,y)
