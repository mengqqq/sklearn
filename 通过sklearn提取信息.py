#import LinearRegression,create regression(name it reg) and fit it to the training data
from sklearn.Linear_model import LinearRegression
reg=LinearRegression()
reg.fit(ages_train,net_worths_train)

print "Katie's net worth prediction:",reg.predict([27])
print "slope:",reg.coef_
print "intercept:",reg.intercept_

print "\n ##### stats on test dataset########\n"
print "r-squared score:", reg.score(ages_test,net_worths_test)
print "\n ####stats on training dataset ########\n"
print "r-squared score:",reg.score(ages_train,net_worths_train)
