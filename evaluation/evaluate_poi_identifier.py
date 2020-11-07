#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(
    features, labels, test_size = 0.3, random_state = 42)

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
print clf.score(features_test, labels_test)
print sum(clf.predict(features_test))
print len(clf.predict(features_test))
for i in range(len(features_test)):
    if clf.predict(features_test[i].reshape(-1,1)) == 1 and labels_test[i] == 1:
        print "TRUE POSITIVE"

from sklearn.metrics import precision_score, recall_score
print precision_score(labels_test, clf.predict(features_test))
print recall_score(labels_test, clf.predict(features_test))
