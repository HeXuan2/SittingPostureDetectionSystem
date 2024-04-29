import pandas as pd
import numpy as np
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import SelectFromModel
import joblib

# 读取数据
df = pd.read_excel('../data/CrossLegTotal.xlsx')
# 获取输入特征与目标标签
x_data = df[['distance1', 'distance2', 'distance3', 'distance4','distance5', 'distance6']].values
y_data = df['label'].values
# 训练测试切分
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2)
# 调参选择最佳参数
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_features': [0.6, 0.8, 1.0]
}
grid_search = GridSearchCV(RandomForestClassifier(), param_grid, scoring='accuracy', cv=5)
grid_search.fit(x_train, y_train)
# 构建最佳模型
rf = grid_search.best_estimator_
rf.fit(x_train, y_train)
# 模型预测
print(x_test)
y_pred = rf.predict(x_test)
print(y_pred)
# 模型评估
accuracy = round(rf.score(x_test, y_test) * 100, 2)
print('随机森林模型精度:%.2f%%' % accuracy)
# 模型序列化
joblib.dump(rf, 'rf_model_CrossLeg_1.joblib')