import pandas as pd
# from skmultilearn.problem_transform import LabelPowerset
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier

df = pd.read_csv('datasets/train/new_data2.csv')

features = df[['pitch', 'yaw', 'roll', 'relative_distance', 'HunchValue']]
labels = df['target']
mlb = MultiLabelBinarizer()
labels_encoded = mlb.fit_transform(labels.apply(lambda x: x.split(', ')))

# 特征选择
xgb = XGBClassifier()
xgb.fit(features, labels_encoded)
importance = xgb.feature_importances_
threshold = 0.05  # 设置特征重要性阈值
selected_features = features.columns[importance > threshold]  #选择特征评估指标＞阈值的特征
selected_features_data = features[selected_features]

X_train, X_test, y_train, y_test = train_test_split(selected_features_data, labels_encoded, random_state=0)

clf_multilabel = OneVsRestClassifier(XGBClassifier(
    objective='multi:softprob',  # 使用'multi:softprob'作为损失函数
    num_class=5,  # 标签的数量
    n_estimators=75,  #
    max_depth=8,
    learning_rate=0.3
))

clf_multilabel.fit(X_train, y_train)

prediction = clf_multilabel.predict(X_test)
score = metrics.accuracy_score(prediction, y_test)
print(score)



