
class Transform():
    def __init__(self):
        pass
    #xlsx to csv
    def XtoC(self,data,name):
        self.data = data
        self.name = name
        self.data.to_csv('datasets/train/'+self.name+'.csv', index=False)
    #打标签
    def StoM(self,data,name):
        self.data = data
        self.name = name

        self.grouped_data = self.data.groupby(self.data.columns[:-1].tolist(), as_index=False)['target'].agg(list)
        self.grouped_data['target'] = self.grouped_data['target'].apply(lambda x: ', '.join(x))

        self.grouped_data.to_csv('datasets/train/'+self.name+'_ml.csv', index=False)

