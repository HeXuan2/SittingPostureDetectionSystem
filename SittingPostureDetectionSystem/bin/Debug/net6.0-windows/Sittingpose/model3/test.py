def main():
    import matplotlib.pyplot as plt
    import pandas as pd
    from DataTransform import Transform
    from Model_train import SL_Model
    from Model_train import ML_Model
    import joblib


    # 格式转换，xlsx转换成csv
    data0 = pd.read_excel('../data/head123total.xlsx')
    name = 'testdataHead'
    Tran = Transform()
    Tran.XtoC(data0,name)

    data = pd.read_csv('datasets/'+name+'.csv')

    #建模
    sl_model = SL_Model(data,fea_start=2,fea_end=5)
    score_mean = sl_model.score_mean()
    print("score_mean",score_mean)
    fit_model, high_score = sl_model.select_model()
    print("head123total：fit_model, high_score",fit_model, high_score)
    joblib.dump(fit_model, 'model/ModelHead.pkl')


    # 格式转换，xlsx转换成csv
    data0 = pd.read_excel('../data/HunchTotal.xlsx')
    name = 'testdataHunch'
    Tran = Transform()
    Tran.XtoC(data0, name)
    # 数据可视化分析
    data = pd.read_csv('datasets/' + name + '.csv')

    # 建模
    sl_model = SL_Model(data, fea_start=2, fea_end=5)
    score_mean = sl_model.score_mean()
    print("score_mean", score_mean)
    fit_model, high_score = sl_model.select_model()
    print("Hunch4Total：fit_model, high_score", fit_model, high_score)
    joblib.dump(fit_model, 'model/ModelHunch.pkl')

    # 格式转换，xlsx转换成csv
    data0 = pd.read_excel('../data/CrossLegTotal.xlsx')
    name = 'testdataCrossLeg'
    Tran = Transform()
    Tran.XtoC(data0, name)
    # 数据可视化分析
    data = pd.read_csv('datasets/' + name + '.csv')

    # 建模
    sl_model = SL_Model(data, fea_start=2, fea_end=6)
    score_mean = sl_model.score_mean()
    print("score_mean", score_mean)
    fit_model, high_score = sl_model.select_model()
    print("CrossLeg5Total：fit_model, high_score", fit_model, high_score)
    joblib.dump(fit_model, 'model/ModelCrossLeg.pkl')





if __name__ == '__main__':
    main()