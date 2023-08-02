from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

# load the iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# train a random forest classifier
clf = RandomForestClassifier()
clf.fit(X, y)

# save the model
pickle.dump(clf, open("iris_model.pkl", "wb"))
