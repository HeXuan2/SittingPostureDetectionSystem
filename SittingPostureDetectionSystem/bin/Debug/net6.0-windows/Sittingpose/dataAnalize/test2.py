import joblib
from sklearn.preprocessing import MultiLabelBinarizer
from xgboost import XGBClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import metrics

df = pd.read_csv('datasets/train/new_data1.csv')
features = df[['pitch', 'yaw', 'roll', 'relative_distance', 'HunchValue']]
labels = df['target']
mlb = MultiLabelBinarizer()
a = df.describe()
print(str(a))