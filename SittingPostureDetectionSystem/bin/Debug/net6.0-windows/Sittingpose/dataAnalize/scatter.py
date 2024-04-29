import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#文件夹路径
filePath = './excel/'
#路径  1,2,3
fileNameList = ['head123total.xlsx', 'Hunch4Total.xlsx', 'CrossLeg5Total.xlsx']

'''直方图'''
def DistPlot(data, name, label):                #文件路径 特征值['pitch'...] 标签[0,1,2...]
    dataInNeed = data.loc[data['label'] == label, [name]]   #读取相同label的列数据
    sns.distplot(list(dataInNeed[name]))                    #直方图
    plt.title(str(label) + '_' + name)                      #命名
    plt.show()                                              #绘制


for fileName in fileNameList:
    path = filePath + fileName          #文件路径
    data = pd.read_excel(path)          #读取excel数据
    nameList = list(data)               #表头列表
    labelSet = set(data['label'])       #label集合
    for label in labelSet:
        for name in nameList[2:]:
            DistPlot(data, name, label)

'''散点图'''
def PairPlot(path):
    data = pd.read_excel(path)                      #读取数据
    sns.pairplot(data.iloc[:, 1:], hue = 'label')   #散点图
    plt.show()

for fileName in fileNameList:
    path = filePath + fileName          #文件路径
    PairPlot(path)

'''箱线图'''
def BoxPlot(path):
    data = pd.read_excel(path)                          #读取数据
    nameList = list(data)[2:]                           #表头
    for name in nameList:
        sns.boxplot(x = 'label', y = name, data = data) #箱线图
        plt.show()


for fileName in fileNameList:
    path = filePath + fileName          #文件路径
    BoxPlot(path)
plt.show()