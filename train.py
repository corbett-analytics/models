import joblib
from sklearn.datasets import load_iris
from sklearn import tree


X, y = load_iris(return_X_y=True)
clf = tree.DecisionTreeClassifier()
model = clf.fit(X, y)
joblib.dump(model,  'iris.joblib')
