""" Resources: 
sklearn module: http://scikit-learn.org/stable/modules/classes.html#module-sklearn.tree
decision tree: http://scikit-learn.org/stable/modules/tree.html
decision tree: http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier.score
example (ayos to): http://christianherta.de/lehre/dataScience/machineLearning/decision-trees.php
example: http://chrisstrelioff.ws/sandbox/2015/06/08/decision_trees_in_python_with_scikit_learn_and_pandas.html
gini vs entropy: http://haohanw.blogspot.com/2014/08/ml-decision-tree-rule-selection.html
stratifiedshufflesplit: http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html
extratrees: http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier
decision tree vs extratrees: http://stackoverflow.com/questions/20177970/decisiontreeclassifier-vs-extratreeclassifier
"""
import csv
from os import sys
import pandas as pd
import numpy as np
import pydotplus
from sklearn import tree
from sklearn.utils import shuffle
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import StratifiedShuffleSplit, train_test_split, StratifiedKFold
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.feature_selection import VarianceThreshold
from sklearn.neural_network import MLPClassifier

#import csv
# df = pd.read_csv("StressCheck.csv") #100 samples
# df = pd.read_csv("StressCheck2.csv") #400 samples
df = pd.read_csv("StressCheck3.csv") #experimental samples
#NOTE: if you change the file name, change mo rin yung nasa baba (writeToCSV())


columns = df.columns.values.tolist()
columns.pop(0) #tinanggal lang yung "diagnosis" kasi di siya part ng features

#set the values for X and Y using 70% of the data set
X =  features = df[list(columns)].values
y =  labels = df["Diagnosis"].values
X_train = X_test = df[list(columns)].values
y_train = y_test = df["Diagnosis"].values

#pang tanggal sana ng low variant features
#PERO HINDI NAMAN GUMAGANA ANUBAAAAAAAAAAA :(
# sel = VarianceThreshold(threshold=(.8*(1-.8)))
# sel.fit_transform(X)
# print "no. features", len(X[0])

#shuffle and split data into training and testing sets
# 70% train size, 30% test size
sss = StratifiedShuffleSplit(n_splits=10, test_size=.30, random_state=0)
for train_index, test_index in sss.split(X, y):
	# print("TRAIN:", train_index, "TEST:", test_index)
	X_train, X_test = X[train_index], X[test_index]
	y_train, y_test = y[train_index], y[test_index]


#---- TRAINING ----#

# #Now we are ready to learn a decision tree
# clf = tree.DecisionTreeClassifier(criterion="gini") #gini or entropy
clf = ExtraTreesClassifier(n_estimators=1500, max_features=1,criterion="entropy",verbose=0,bootstrap=1,oob_score=1)
# clf = tree.ExtraTreeClassifier(max_features=1,criterion="entropy")
# clf = RandomForestClassifier()
# clf = MLPClassifier()
clf = clf.fit(X_train, y_train)

# the decision tree can be visualized. 
# produce an image.png of tree
# dot_data = tree.export_graphviz(clf, out_file=None, 
# 									feature_names=columns, 
# 									class_names=labels, 
# 									rounded=True, filled=True)
# graph = pydotplus.graph_from_dot_data(dot_data) 
# graph.write_png("StressCheck.png")


#---- TESTING ----#
def Testing():

	pred = clf.predict(X_test)

	print (classification_report(y_test,pred))
	print (confusion_matrix(y_test,pred))
	print "score:", clf.score(X_test,y_test) 

#--- para sa software ---#
def Predicting(array=[[0,0,1,1,1,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,1]]):
	Z = array
	pred = clf.predict(Z)
	print pred[0]
	return pred[0]

# writes the data gathered from using the software
## wag muna tong gamitin. para sa exhibit itechi. or sa demo rin pala
def writeToCSV(array, yesno, predAns, truAns):
	with open('StressCheck3.csv', 'a') as csvfile: #NOTE: if you change the filename, change mo din yung nasa taas
		writer = csv.writer(csvfile)
		if yesno == 1:
			array.insert(0,predAns)
		else:
			array.insert(1,truAns)
		writer.writerow(array)


#---UNIT TESTS---# 
# for the 10 user testing required; creates a separate file
# array: ito yung sagot nila [0,1,...,1,1]
# yesno: ito yung "Was this correct/helpful?"
# predAns: ito yung result ni StressCheckUp
# truAns: ito yung sagot talaga ni user (may be same sa predAns)
def unitTestWrite(array, yesno, predAns, truAns):
	with open('unittests.csv', 'a') as csvfile:
		writer = csv.writer(csvfile)
		if yesno == 1:
			array.insert(0,predAns)
		else:
			array.insert(1,truAns)
		writer.writerow(array)

def unitTesting():
	df2 = pd.read_csv("unittests.csv")
	X_test = df2[list(columns)].values
	y_test = df2["Diagnosis"].values
	pred = clf.predict(X_test)

	print (classification_report(y_test,pred))
	print (confusion_matrix(y_test,pred))
	print "score:", clf.score(X_test,y_test) 
	

#--- terminal stuff ---#
if len(sys.argv) > 1:
	if sys.argv[1] == "test":
		Testing()
	elif sys.argv[1] == "pred":
		Predicting()
	elif sys.argv[1] == "utest":
		unitTesting()