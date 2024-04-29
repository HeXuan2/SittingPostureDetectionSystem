from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from xgboost import XGBClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

class ML_Model():
    def __init__(self,data,fea_start,fea_end,targetname = 'label'):
        self.data = data
        #数据处理
        self.features = self.data.iloc[:,fea_start:fea_end]
        self.labels = self.data[targetname]
        self.mlb = MultiLabelBinarizer()
        self.labels_encoded = self.mlb.fit_transform(self.labels.apply(lambda x: x.split(', ')))

    def ml_model(self,threshold=0.02,labelcount=5,tree_num=50,tree_depth=6,learning_rates=0.1):
        #XGBoost作为基分类器
        self.xgb = XGBClassifier()
        self.xgb.fit(self.features, self.labels_encoded)
        self.importance = self.xgb.feature_importances_
        self.threshold = threshold  # 设置特征重要性阈值
        self.selected_features = self.features.columns[self.importance > self.threshold]  # 选择特征评估指标＞阈值的特征
        self.selected_features_data = self.features[self.selected_features]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.selected_features_data, self.labels_encoded, random_state=0)
        self.clf_multilabel = OneVsRestClassifier(XGBClassifier(
            objective='multi:softprob',  # 使用'multi:softprob'作为损失函数
            num_class=labelcount,  # 标签的数量
            n_estimators=tree_num,
            max_depth=tree_depth,
            learning_rate=learning_rates
        ))

        self.clf_multilabel.fit(self.X_train, self.y_train)
        self.prediction = self.clf_multilabel.predict(self.X_test)
        self.score = metrics.accuracy_score(self.prediction, self.y_test)

        return self.clf_multilabel,self.score,self.mlb


class SL_Model():
    def __init__(self,data,fea_start,fea_end ,targetname = 'label'):
        self.data = data
        self.x = self.data.iloc[:,fea_start:fea_end]
        self.y = self.data[targetname]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.x, self.y, random_state=0)
    #svm
    def svm_model(self):
        self.model_s = svm.SVC()
        self.model_s.fit(self.X_train,self.y_train)
        self.pre_s = self.model_s.predict(self.X_test)
        self.score_s = metrics.accuracy_score(self.pre_s,self.y_test)
        print("self.model_s,self.score_s",self.model_s,self.score_s)
        return self.model_s,self.score_s

    #logistic
    def log_model(self):
        self.model_l = LogisticRegression(max_iter=300)
        self.model_l.fit(self.X_train,self.y_train)
        self.pre_l = self.model_l.predict(self.X_test)
        self.score_l = metrics.accuracy_score(self.pre_l,self.y_test)
        print("self.model_l,self.score_l", self.model_l, self.score_l)
        return self.model_l,self.score_l

    #decision tree
    def dec_model(self):
        self.model_d = DecisionTreeClassifier()
        self.model_d.fit(self.X_train,self.y_train)
        self.pre_d = self.model_d.predict(self.X_test)
        self.score_d = metrics.accuracy_score(self.pre_d,self.y_test)
        print("self.model_d,self.score_d",self.model_d,self.score_d)
        return self.model_d,self.score_d

    #k-neighbors
    def k_model(self):
        self.model_k = KNeighborsClassifier(n_neighbors=3)
        self.model_k.fit(self.X_train,self.y_train)
        self.pre_k = self.model_k.predict(self.X_test)
        self.score_k = metrics.accuracy_score(self.pre_k,self.y_test)
        print("self.model_k,self.score_k",self.model_k,self.score_k)
        return self.model_k,self.score_k

    #构建随机森林模型
    def r_model(self):
        self.model_r = RandomForestClassifier(n_estimators=100)
        self.model_r.fit(self.X_train, self.y_train)
        self.pre_r = self.model_k.predict(self.X_test)
        self.score_r = metrics.accuracy_score(self.pre_r, self.y_test)
        print("self.model_r,self.score_r", self.model_r, self.score_r)
        return self.model_r, self.score_r


    def score_mean(self):
        _, self.score_s = self.svm_model()
        _, self.score_l = self.log_model()
        _, self.score_d = self.dec_model()
        _, self.score_k = self.k_model()
        _, self.score_r=self.r_model()
        self.mean = (self.score_s+self.score_d+self.score_k+self.score_r)/3
        return self.mean

    #选择模型
    def select_model(self):
        self.model_s, self.score_s = self.svm_model()
        self.model_d, self.score_d = self.dec_model()
        self.model_k, self.score_k = self.k_model()
        self.model_l,self.score_l=self.r_model()
        self.model_r, self.score_r=self.r_model()
        self.max_score = max(self.score_s, self.score_d, self.score_k,self.score_l,self.score_r)

        if self.max_score == self.score_s:
            self.best_model = self.model_s
        elif self.max_score == self.score_d:
            self.best_model = self.model_d
        else:
            self.best_model = self.model_k
        return self.best_model,self.max_score


