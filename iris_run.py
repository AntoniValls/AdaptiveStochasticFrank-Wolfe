"""
Iris Dataset

 The Iris dataset is a classic dataset used in machine learning.
 It contains 150 measurements of four attributes of three species of iris flowers.
 The attributes are: sepal length, sepal width, petal length, and petal width.
 The three species are: Setosa, Versicolor, and Virginica.
 This dataset is often used to practice classification and clustering algorithms. \\
 It's a simple yet popular choice for learning and demonstrating data analysis.
"""

from sklearn import datasets
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from SFW import SFW_NN
from AdaSFW import AdaSFW_NN
from AdaSVRF import AdaSVRF_NN

# Load iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target
num_classes = len(set(y)) # Number of classification labels

# Binarize the outputs
y = LabelBinarizer().fit_transform(y)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

"""### 2.1.1 SFW:"""

SFW_iris = SFW_NN(X_train, y_train, X_test, y_test, initfactor = 20)
SFW_iris.train()
SFW_iris.test()
SFW_iris.plot_learning_curves()

SFW_iris.plot_2D_update()

"""### 2.1.2 AdaSFW

"""

AdaSFW_iris = AdaSFW_NN(X_train, y_train, X_test, y_test, initfactor = 20)
AdaSFW_iris.train()
AdaSFW_iris.test()
AdaSFW_iris.plot_learning_curves()

AdaSFW_iris.plot_2D_update()

"""### 2.1.3 AdaSVRF"""

AdaSVRF_iris = AdaSVRF_NN(X_train, y_train, X_test, y_test, initfactor = 20, nu = 10**(-1/2), K = 5)
AdaSVRF_iris.train()
AdaSVRF_iris.test()
AdaSVRF_iris.plot_learning_curves()

AdaSVRF_iris.plot_2D_update()
