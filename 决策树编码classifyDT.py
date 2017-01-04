def classify(features_train,labels_train):
    from sklearn import tree
    
    clf=tree.DecisionTreeClassifier()
    clf=clf.fit(features_train,labels_train)
    clf.predict(features_train)
    ###your code goes here---should return a trained decision tree classifer
    
    return clf
    
    
    
