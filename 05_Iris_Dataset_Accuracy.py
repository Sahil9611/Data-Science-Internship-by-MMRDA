'''STEPS uses while apply any algorithm
1-import watever we need
2-create instanances
3-identifing X and Y
4-split the data into training and testing
5-Train the algorithm/model and test the algorithm/model
6-check the accuracy'''

import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import MultinomialNB

df=pd.read_csv("E:/User Sahil/Desktop/Data Science/IRIS.csv")

rf=RandomForestClassifier(random_state=1)
lr=LogisticRegression(random_state=0)
gbm=GradientBoostingClassifier(n_estimators=10)
dt=DecisionTreeClassifier(random_state=0)
sv=svm.SVC()
nn=MLPClassifier(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(5,2),random_state=0)
nb=MultinomialNB()

X = df.drop("species",axis=1)
Y = df["species"]
#print(X)
#print(Y)


X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=0,test_size=0.3)

rf_train = rf.fit(X_train,Y_train)
rf_pred = rf.predict(X_test)

lr_train = lr.fit(X_train,Y_train)
lr_pred = lr.predict(X_test)

gbm_train = gbm.fit(X_train,Y_train)
gbm_pred = gbm.predict(X_test)

dt_train = dt.fit(X_train,Y_train)
dt_pred = dt.predict(X_test)

sv_train = sv.fit(X_train,Y_train)
sv_pred = sv.predict(X_test)

nn_train = nn.fit(X_train,Y_train)
nn_pred = nn.predict(X_test)

nb_train = nb.fit(X_train,Y_train)
nb_pred = nb.predict(X_test)

print('Random Forest:-')
print(accuracy_score(Y_test,  rf_pred))

print('Logistic Regression:-')
print(accuracy_score(Y_test,  lr_pred))

print('Gradient Boosting Classifier:-')
print(accuracy_score(Y_test,  gbm_pred))

print('Decision Tree Classifier:-')
print(accuracy_score(Y_test,  dt_pred))

print('SVM:-')
print(accuracy_score(Y_test,  sv_pred))

print('MLPClassifier:-')
print(accuracy_score(Y_test,  nn_pred))

print('NaiveBayes:-')
print(accuracy_score(Y_test,  nb_pred))


'''Output:-

Random Forest:-
0.9777777777777777
Logistic Regression:-
0.9777777777777777
Gradient Boosting Classifier:-
0.9777777777777777
Decision Tree Classifier:-
0.9777777777777777
SVM:-
0.9777777777777777
MLPClassifier:-
0.24444444444444444
NaiveBayes:-
0.6
'''