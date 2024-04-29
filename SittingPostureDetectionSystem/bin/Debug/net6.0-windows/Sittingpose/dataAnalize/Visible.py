import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class DrawGraph():

    def __init__(self,data,name):
        self.data = data
        self.name = name
    #直方图
    def draw_hist(self,columnname,indexname='target',bin = 8,imagename='img'):
        #self.data.set_index(indexname,inplace=True)
        plt.hist(self.data[columnname], bins=bin)
        plt.xlabel(columnname)
        plt.savefig('img/train/'+imagename+'_hist.png')

    #柱形图
    def draw_coldiagram(self,x,y,xlabel=None,ylabel=None):
        plt.bar(x, y)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.savefig('img/train/'+self.name+'_bar.png')

    #饼图
    def draw_circular_scale(self,kinds_list,scale_list,name=None,dev_list=None):
        kinds = kinds_list
        iris_kind_scale = scale_list
        #间隔
        self.dev_position = dev_list
        plt.pie(iris_kind_scale, labels=kinds, autopct='%3.1f%%', shadow=True, explode=self.dev_position, startangle=90)
        plt.title('Circular_scale')
        plt.savefig('img/train/'+self.name+'_scale.png')

    #箱线图
    def draw_boxplot(self):
        self.data.boxplot(figsize=(12, 9))
        plt.title('boxplot')
        plt.savefig('img/train/'+self.name+'_boxplot.png')

    #每两种特征的散点图
    def draw_scatter_matrix(self):
        pd.plotting.scatter_matrix(self.data, alpha=0.8, figsize=(10, 10))
        plt.savefig('img/train/'+self.name+'_scatter_matrix.png')

    #热图
    def draw_heatmap(self):
        self.correlation_matrix = self.data.corr()
        plt.figure(figsize=(12, 9))
        sns.heatmap(self.correlation_matrix, annot=True, fmt='.3f')
        plt.savefig('img/train/'+self.name+'_heat_map.png')

    #散点图
    def draw_scatter(self,fea1,fea2):
        plt.scatter(self.data[fea1], self.data[fea2], alpha=1.0, color='k')
        plt.xlabel(fea1)
        plt.ylabel(fea2)
        plt.savefig('img/train/'+self.name+'_scatter.png')

    #特征和标签之间的散点图
    def draw_f_t_sca(self,targetname = 'target'):
        self.fig, self.axes = plt.subplots(nrows=1, ncols=len(self.data.columns) - 1, figsize=(30, 4))
        # 遍历每个特征
        for i, feature in enumerate(self.data.columns[1:]):
            # 绘制散点图
            self.axes[i].scatter(self.data[feature], self.data[targetname], alpha=1.0, color='k')
            self.axes[i].set_xlabel(feature)
            self.axes[i].set_ylabel('label')
        # 调整子图之间的间距
        plt.tight_layout()
        plt.savefig('img/train/'+self.name+'lab-cha_scatter.png')

    #折线图
    def draw_plot(self):
        self.data.plot()
        plt.savefig('img/train/'+self.name+'plot.png')

    def draw_pointplot(self,X='target',Y=None,imagename='img'):
        sns.pointplot(x=X,y=Y,data=self.data)
        plt.savefig('img/train/'+imagename+'_pointplot.png')

    def draw_common(self):
        self.draw_boxplot()
        self.draw_f_t_sca()
        self.draw_heatmap()
        self.draw_scatter_matrix()
        self.draw_plot()






