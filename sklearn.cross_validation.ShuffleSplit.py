from sklearn import cross_validation
rs=cross_validation.ShuffleSplit(4,n_iter=3,test_size=.25,random_state=0)
len(rs)  //3
print(rs) //ShuffleSplit(4,n_iter=3,test_size=0.25,....)
for train_index,test_index in rs:
    print("TRAIN:",train_index,"TEST:",test_index)
rs=cross_validation.ShuffleSplit(4,n_iter=3,train_size=0.5,test_size=.25,random_state=0)
for train_index,test_index in rs:
    print("TRAIN:", train_index,"TEST:",test_index)

    
