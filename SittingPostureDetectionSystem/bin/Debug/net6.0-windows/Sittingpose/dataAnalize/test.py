import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import model_selection
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from Visible import DrawGraph


data = pd.read_csv('datasets/train/new_data1.csv')
target = data['target'].value_counts()
label = target.index.tolist()
count = target.values.tolist()


sns.pointplot(x='target',y='yaw')
plt.show()

#多标签分列
# data = pd.read_csv('datasets/train/new_data1.csv')
# data.to_excel('datasets/train/new_data1.xlsx')
#
# data = pd.read_csv('datasets/train/new_data1.xlsx')

data1 =pd.read_csv('datasets/train/new_data1.csv')

draw = DrawGraph(data1)

colunm_name = data1.columns.tolist()

print(colunm_name)

for i in range(len(colunm_name)-1):
    draw.draw_hist(columnname=colunm_name[i],imagename=colunm_name[i])

input_file = 'datasets/train/new_data1.xlsx'
df = pd.read_excel(input_file)

length = len(df['relative_distance'])
increment_range = (1, 6)
increments = np.random.uniform(*increment_range, size=length)
df['relative_distance'] += increments

output_file = 'datasets/train/new_data2.xlsx'
df.to_excel(output_file, index=False)


data = pd.read_csv('datasets/test1_1.csv')
X = data[['pitch','yaw','roll','relative_distance','HunchValue']]
y = data['target']  # 多标签集合，每个元素是一个包含多个标签的列表

X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,random_state=0)
print(X_test.shape)


mlb = MultiLabelBinarizer()
y_binary = mlb.fit_transform(y_train)

classifier = OneVsRestClassifier(LogisticRegression())

# 训练多个二分类模型
classifier.fit(X_train, y_binary)
x_new = X_test
predictions = classifier.predict([x_new])
predicted_labels = mlb.inverse_transform(predictions)
print(predicted_labels)
