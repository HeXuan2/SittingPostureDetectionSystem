import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


data = pd.read_csv('datasets/train/new_data1.csv',usecols=[0,1,2,3,4,5])
#data = data.dropna()
#print(data.head())
#print(data.info)
#print(data.describe())
#载入特征和标签
x = data[['pitch','yaw','roll','relative_distance','HunchValue']]

y = data['target']

# 对标签集进行编码
encoder = LabelEncoder()
y = encoder.fit_transform(y)

#使用主要特征训练
pitch = data[['pitch','target']]
roll = data[['roll','target']]
yaw=data[['yaw','target']]
relative_distance = data[['relative_distance','target']]
hunchvalue = data[['HunchValue','target']]

train_p, test_p = train_test_split(pitch, test_size=0.3, random_state=0)

X_train_p = train_p[['pitch']]
y_train_p = train_p.target
X_test_p = test_p[['pitch']]
y_test_p = test_p.target

train_y, test_y = train_test_split(yaw, test_size=0.3, random_state=0)
X_train_y = train_y[['yaw']]
y_train_y = train_y.target
X_test_y = test_y[['yaw']]
y_test_y = test_y.target

train_r, test_r = train_test_split(roll, test_size=0.3, random_state=0)
X_train_r = train_r[['roll']]
y_train_r = train_r.target
X_test_r = test_r[['roll']]
y_test_r = test_r.target

train_re, test_re = train_test_split(relative_distance, test_size=0.3, random_state=0)
X_train_re = train_re[['relative_distance']]
y_train_re = train_re.target
X_test_re = test_re[['relative_distance']]
y_test_re = test_re.target

train_h, test_h = train_test_split(hunchvalue, test_size=0.3, random_state=0)
X_train_h = train_h[['HunchValue']]
y_train_h = train_h.target
X_test_h = test_h[['HunchValue']]
y_test_h = test_h.target

#k-neighbors
model=KNeighborsClassifier(n_neighbors=3)
model.fit(X_train_p, y_train_p)
prediction = model.predict(X_test_p)
print('The accuracy of the KNN using pitch is: {:.3f}'.format(metrics.accuracy_score(prediction, y_test_p)))

model2=KNeighborsClassifier(n_neighbors=3)
model2.fit(X_train_y, y_train_y)
prediction = model2.predict(X_test_y)
print('The accuracy of the KNN using yaw is: {:.3f}'.format(metrics.accuracy_score(prediction, y_test_y)))



